
class _Node:
    def __init__(self, value:str, is_leaf:bool = False) -> None:
        self.value = value
        self.is_leaf = is_leaf
        self.branches = {}
        self.string = f"|__{value}"


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
    
    def _contained_part_split(self, key:str, index:int=1) -> tuple[str, str]:
        if not self.contains(key[:index]):
            return key[:index-1], key[index-1:]
        return self._contained_part_split(key, index + 1)
    
    def _add_key_to(node:_Node, key:str) -> None:
        node.branches[key[0]] = _Node(key[0], len(key)==1)
        if len(key) > 1:
            Trie._add_key_to(node.branches[key[0]], key[1:])
    
    def _get_node(node:_Node, branch:str) -> _Node:
        if not branch:
            return node
        if len(branch) == 1:
            return node.branches[branch]
        return Trie._get_node(node.branches[branch[0]], branch[1:])

    def add(self, key:str) -> None:
        if not self.contains(key):
            contained, new_part = self._contained_part_split(key)
            return Trie._add_key_to(Trie._get_node(self.head, contained), new_part)
    
    def _node_str(node:_Node, genealogy="", brothers_nb=0, word="") -> str:
        next_genealogy = f"{genealogy}{"|  " if brothers_nb else "   "}"
        if_node_is_leaf  = f" *[{word}{node.value}]\n{next_genealogy + ("|" if node.branches else "")}" if node.is_leaf else ""
        brothers_nb = len(node.branches)-1
        return f"{genealogy}{node.string}{if_node_is_leaf}\n{"".join(Trie._node_str(node.branches[key], next_genealogy, brothers_nb-i, word+node.value) for i, key in enumerate(node.branches))}"

    def __str__(self) -> str:
        return Trie._node_str(self.head)
            


# ==================================================== #
#                       TESTS                          #
# ==================================================== #
if __name__ == "__main__":
    # t1, t2 = Trie(), Trie()
    # print(f"{id(Trie._get_node) =}")
    # print(f"{id(t1.add) = }\n{id(t1._get_node) = }\n{id(t1.head) = }\n")
    # print(f"{id(t2.add) = }\n{id(t2._get_node) = }\n{id(t2.head) = }")

    trie = Trie()

    to_add_keys_list = [
        "à",
        "arbre",
        "art", "artiste",
        "chape", "chapeau",
        "créatif", "création",
        "œuf",
        "zèbre"
    ]

    for key in to_add_keys_list:
        trie.add(key)

    print(trie)