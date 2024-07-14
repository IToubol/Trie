
class _Node:
    def __init__(self, value:str, is_leaf:bool = False) -> None:
        self.value = value
        self.is_leaf = is_leaf
        self.branches = {}

    def __str__(self) -> str:
        return f"|__{self.value}"


class Trie:
    def __init__(self) -> None:
        self.head = _Node("")

    def _found_in(node:_Node, key:str) -> bool:
        if key[0] in node.branches:
            if len(key) > 1:
                return Trie._found_in(node.branches[key[0]], key[1:])
            return True
        return False

    def contains(self, key:str) -> bool:
        return Trie._found_in(self.head, key)
    
    def _contained_part_split(node: _Node, key:str, index:int=1) -> tuple[str, str]:
        if not Trie._found_in(node, key[:index]):
            return key[:index-1], key[index-1:]
        return Trie._contained_part_split(node, key, index + 1)
    
    def _add_key_to(node:_Node, key:str) -> None:
        node.branches[key[0]] = _Node(key[0], len(key)==1)
        if len(key) > 1:
            Trie._add_key_to(node.branches[key[0]], key[1:])
    
    def _end_of_branch(node:_Node, branch:str) -> _Node:
        if not branch:
            return node
        if len(branch) == 1:
            return node.branches[branch]
        return Trie._end_of_branch(node.branches[branch[0]], branch[1:])

    def add(self, key:str) -> None:
        if not self.contains(key):
            contained, new_part = Trie._contained_part_split(self.head, key)
            return Trie._add_key_to(Trie._end_of_branch(self.head, contained), new_part)
    
    def _displaying(node:_Node, genealogy="", remaining_brothers_nb=0, word="") -> str:
        next_genealogy = f"{genealogy}{"|  " if remaining_brothers_nb else "   "}"
        leaf_part  = f" *[{word}{node.value}]\n{next_genealogy + ("|" if node.branches else "")}" if node.is_leaf else ""
        sons_nb = len(node.branches)-1
        return f"{genealogy}{node.__str__()}{leaf_part}\n{"".join(Trie._displaying(node.branches[key], next_genealogy, sons_nb-i, word+node.value) for i, key in enumerate(node.branches))}"

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

    trie = Trie()

    to_add_keys_list = [
        "à",
        "arbre", "arbuste", "arbustes",
        "art", "artiste",
        "chape", "chapeau", "chapelle",
        "créatif", "création", "créance", "créancier",
        "œuf",
        "zèbre"
    ]

    for key in to_add_keys_list:
        trie.add(key)

    print(trie)