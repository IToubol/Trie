from typing import TypeVar

TNode = TypeVar("TNode", bound="Trie")

class Trie:
    def __init__(self, value:str="") -> None:
        self.value    = value
        self.branches = set()
        self.is_leaf  = True

    def __getitem__(self, key:str) -> TNode:
        if key:
            for node in self.branches:
                if node.value == key[0]:
                    return node[key[1:]]
            raise KeyError(f"Key {key} not found ")
        return self

    def __contains__(self, key:str) -> bool:
        for node in self.branches:
            if node.value == key[0]:
                if len(key) == 1:
                    return True
                return key[1:] in node
        return False

    def _present_absent_split(self, key:str, index:int=1) -> tuple[str, str]:
        if key[:index] in self:
            return self._present_absent_split(key, index + 1)            
        return key[:index-1], key[index-1:]

    def extend(self, key:str) -> None:
        present, absent = self._present_absent_split(key)
        if absent:
            self.is_leaf = False
            new_node = Trie(absent[0])
            self[present].branches.add(new_node)
            new_node.extend(absent[1:])

    def __str__(self, genealogy:str="", accumulated:str="", remaining_siblings_nb:int=0) -> str:
        """
        Generates a textual representation of a node and its descendants in a trie (prefix tree).

        This recursive function builds a string representing the tree structure
        from the given node, using ASCII characters to visualize parent-child
        relationships and branches.

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
        return f"{genealogy}|{("__" + self.value) if self.value else ""}{(" *[" + next_cumul + "]") if self.is_leaf else ""}\n{"".join(node.__str__(next_line_genealogy, next_cumul, sons_nb-n) for n, node in enumerate(self.branches))}"


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