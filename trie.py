from typing import TypeVar

TNode = TypeVar("TNode", bound="_Node")

class _Node:
    def __init__(self, value:str, is_leaf:bool = False) -> None:
        self.value = value
        self.is_leaf = is_leaf
        self.branches = {}


class Trie:
    def __init__(self) -> None:
        self.head = _Node("")

    @staticmethod
    def _found_in(node:TNode, key:str) -> bool:
        if key[0] in node.branches:
            if len(key) > 1:
                return Trie._found_in(node.branches[key[0]], key[1:])
            return True
        return False

    # def __contains__(self, key:str) -> bool:
    #     return Trie._found_in(self.head, key)

    @staticmethod    
    def _contained_part_split(node:TNode, key:str, index:int=1) -> tuple[str, str]:
        if not Trie._found_in(node, key[:index]):
            return key[:index-1], key[index-1:]
        return Trie._contained_part_split(node, key, index + 1)

    @staticmethod
    def _add_key_to(node:TNode, key:str) -> None:
        node.branches[key[0]] = _Node(key[0], (is_leaf := len(key)==1))
        if not is_leaf:
            Trie._add_key_to(node.branches[key[0]], key[1:])

    @staticmethod
    def _end_of_branch(node:TNode, branch:str) -> TNode:
        if not branch: # needed verification for the case where `contained` in add method is empty
            return node
        if len(branch) == 1:
            return node.branches[branch]
        return Trie._end_of_branch(node.branches[branch[0]], branch[1:])

    def add(self, key:str) -> None:
        contained, new_part = Trie._contained_part_split(self.head, key)
        if key != contained:
            return Trie._add_key_to(Trie._end_of_branch(self.head, contained), new_part)

    @staticmethod
    def _displaying(node:TNode, genealogy="", accumulated="", remaining_siblings_nb=0) -> str:
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
        next_cumul = accumulated + node.value
        next_line_genealogy = f"{genealogy}{"|  " if remaining_siblings_nb else "   " if node.value else ""}"
        sons_nb = len(node.branches)-1
        return f"{genealogy}|{("__" + node.value) if node.value else ""}{(" *[" + next_cumul + "]") if node.is_leaf else ""}\n{"".join(Trie._displaying(node.branches[key], next_line_genealogy, next_cumul, sons_nb-n) for n, key in enumerate(node.branches))}"

    def __str__(self) -> str:
        return Trie._displaying(self.head)
            


# ==================================================== #
#                       TESTS                          #
# ==================================================== #
if __name__ == "__main__":
    # t1, t2 = Trie(), Trie()
    # print(f"{id(Trie._end_of_branch) =}")
    # print(f"{id(t1.add) = }\n{id(t1._end_of_branch) = }\n{id(t1.head) = }\n")
    # print(f"{id(t2.add) = }\n{id(t2._end_of_branch) = }\n{id(t2.head) = }")

    to_add_keys_list = [
        "carotte",
        "à",
        "arbre", "arbuste", "arbustes",
        "art", "artiste",
        "chape", "chapeau", "chaperon",
        "chaud", "chaude", "chauds", "chaudes", "chaudement",
        "créatif", "création", "créance", "créancier",
        "œuf",
        "zèbre",
    ]

    trie = Trie()
    for key in to_add_keys_list:
        trie.add(key)
    print(trie)