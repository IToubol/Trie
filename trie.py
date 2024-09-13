from typing import Generator, NoReturn, TypeVar

TNode = TypeVar("TNode", bound="Trie")

class Trie:
    def __init__(self, value:str="", parent:TNode|None=None) -> None:
        self.value    = value
        self.is_leaf  = False
        self.parent   = parent
        self.branches = {}

    def __getitem__(self, key:str) -> TNode|NoReturn:
        return self.branches[key[0]][key[1:]] if key else self

    def __contains__(self, key:str) -> bool:
        return (char := key[0]) in self.branches and ((len(key) == 1) or key[1:] in self.branches[char])

    def extend(self, key:str) -> None:
        if key:
            if (char := key[0]) in self:
                return self[char].extend(key[1:])

            new_node = Trie(char, self)
            self.branches[char] = new_node
            if len(key) > 1:
                new_node.extend(key[1:])
            else:
                new_node.is_leaf = True

        else:
            self.is_leaf = True

    def remove_key(self, key:str|None=None) -> None:
        if key:
            self[key[0]].remove_key(key[1:])
        elif self.branches:
            self.is_leaf = False
        elif self.parent:
            del self.parent.branches[self]
            self.parent.remove_key()

    def completions(self) -> Generator:
        for node in self.branches.values():
            if node.is_leaf:
                yield node.value
            yield from (node.value + value for value in node.completions())
                

    def __str__(self, genealogy:str="", accumulated:str="", remaining_siblings_nb:int=0) -> str:
        """
        Generates a textual representation of a node and its descendants in a trie (prefix tree).

        This recursive function builds a string
        representing the tree structure of the all trie content,
        to visualize parent-child relationships and branches.

        Args:
            node (TNode): The current node to display.
            genealogy (str, optional): The string representing the "genealogy" of the current node. Defaults to "".
            word (str, optional): The accumulated prefix up to the current node. Defaults to "".
            remaining_brothers_nb (int, optional): The number of remaining siblings of the current node. Defaults to 0.
        Returns:
            str: A string representing the tree structure from the given node.
        """
        next_cumul = accumulated + self.value
        next_line_genealogy = f"{genealogy}{"|  " if remaining_siblings_nb else "   " if self.value else ""}"
        sons_nb = len(self.branches)-1
        return f"{genealogy}|{("__" + self.value) if self.value else ""}{(" *[" + next_cumul + "]") if self.is_leaf else ""}\n{"".join(node.__str__(next_line_genealogy, next_cumul, sons_nb-n) for n, node in enumerate(self.branches.values()))}"


# ==================================================== #
#                       TESTS                          #
# ==================================================== #
if __name__ == "__main__":

    to_add_keys_list = [
        "carotte",
        "à",
        "arbre", "arbuste", "arbustes",
        "art", "artiste",
        "chape", "chapeau", "pomme", "chaperon",
        "chaud", "chaude", "chauds", "chaudes", "chaudement",
        "créatif", "création", "créance", "créancier",
        "œuf",
        "zèbre",
    ]

    trie = Trie()

    for key in to_add_keys_list:
        trie.extend(key)

    print(trie)

    # trie.remove_key("pomme")
    # trie.remove_key("cha")
    trie.remove_key("chape")
    # trie.remove_key("chaudement")

    for completion in trie["ch"].completions():
        print("ch" + completion)

    trie.extend("chape")

    print()
    for completion in trie["ch"].completions():
        print("ch" + completion)

    print()
    print("Avion" in trie, "chaud" in trie, "cha" in trie)
