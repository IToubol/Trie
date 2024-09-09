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

    def contains(self, key:str) -> bool:
        return Trie._found_in(self.head, key)

    @staticmethod    
    def _contained_part_split(node:TNode, key:str, index:int=1) -> tuple[str, str]:
        if not Trie._found_in(node, key[:index]):
            return key[:index-1], key[index-1:]
        return Trie._contained_part_split(node, key, index + 1)

    @staticmethod
    def _add_key_to(node:TNode, key:str) -> None:
        node.branches[key[0]] = _Node(key[0], len(key)==1)
        if len(key) > 1:
            Trie._add_key_to(node.branches[key[0]], key[1:])

    @staticmethod
    def _end_of_branch(node:TNode, branch:str) -> TNode:
        if not branch:
            return node
        if len(branch) == 1:
            return node.branches[branch]
        return Trie._end_of_branch(node.branches[branch[0]], branch[1:])

    def add(self, key:str) -> None:
        contained, new_part = Trie._contained_part_split(self.head, key)
        if key != contained:
            return Trie._add_key_to(Trie._end_of_branch(self.head, contained), new_part)

    @staticmethod
    def _displaying(node:TNode, genealogy="", remaining_brothers_nb=0, word="") -> str:
        """
        recursive function to display the entire content of the tree

        args
            node               (TNode) : a _Node object representing the current character of the tree.
            genealogy            (str) : a string representing the `branchs` of the next characters
            remainig_brothers_nb (int) : the number of branchs from the same node.
            word                 (str) : the retrived part of the current word
        
        return
            str : the entire string of characters representing the tree.
        """
        next_genealogy = f"{genealogy}{"|  " if remaining_brothers_nb else "   " if node.value else ""}"
        leaf_part  = f" *[{word}{node.value}]" if node.is_leaf else ""
        sons_nb = len(node.branches)-1

        return f"{genealogy}|{"__" if node.value else ""}{node.value}{leaf_part}\n{"".join(Trie._displaying(node.branches[key], next_genealogy, sons_nb-n, word+node.value) for n, key in enumerate(node.branches))}"

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
        "à",
        "arbre", "arbuste", "arbustes",
        "art", "artiste",
        "chape", "chapeau", "chaperon",
        "chaud", "chaude", "chauds", "chaudes", "chaudement",
        "créatif", "création", "créance", "créancier",
        "œuf",
        "zèbre", "carotte"
    ]

    trie = Trie()
    for key in to_add_keys_list:
        trie.add(key)
    print(trie)