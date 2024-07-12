
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
    others_keys = ["Bonjour", "Aurevoir", "Pomme"]

    for key in to_add_keys_list:
        trie.add(key)

    for key in to_add_keys_list + others_keys:
        print(f"L'arbre (trie) contient le mot {key}: {trie.contains(key)}")

    def display_node(node:_Node, rank=0) -> str:
        return "\n" + "   " * rank + node.string + ("" if node.is_leaf else "".join(display_node(node.branches[key], rank+1) for key in node.branches))
    
    print("".join(display_node(trie.head.branches[key]) for key in trie.head.branches))