from __future__ import annotations

class _Node:
    def __init__(self, value:str) -> None:
        self.value = value
        self.extensions = {}
    
    def extend(self, key:str) -> None:
        next_node = _Node(key[0])
        self.extensions[key[0]] = next_node
        if len(key) > 1:
            next_node.extend(key[1:])

    def contains(self, key:str) -> bool:
        if key[0] == self.value:
            if len(key) > 1:
                if key[1] in self.extensions:
                    return self.extensions[key[1]].contains(key[1:])
                return False
            return True
        return False
    
    def is_leaf(self) -> bool:
        return not bool(self.extensions)
    
    def leaf(self, key:str) -> _Node:
        if len(key) == 1:
            return self
        return self.extensions[key[1]].leaf(key[1:])

    def contained_part_split(self, key:str, index:int=1) -> tuple[str, str]:
        if not self.contains(key[:index]):
            return key[:index-1], key[index-1:]
        return self.contained_part_split(key, index + 1)


class Trie:
    def __init__(self) -> None:
        self.head = {"": _Node("")}

    def contains(self, key:str) -> bool:
        if key[0] in self.head:
            return self.head[key[0]].contains(key)
        return False

    def add(self, key:str) -> None:
        if not self.contains(key):
            if key[0] in self.head:
                contained_part, new_part = self.head[key[0]].contained_part_split(key)
                self.head[key[0]].leaf(contained_part).extend(new_part)
            else:
                node = _Node(key[0])
                self.head[key[0]] = node
                if len(key) > 1:
                    node.extend(key[1:])
            

# ==================================================== #
#                       TESTS                          #
# ==================================================== #
if __name__ == "__main__":
    trie = Trie()

    to_add_keys_list = [
        "à", "arbre", "art", "artiste",
        "chape", "chapeau", "créatif",
        "création", "œuf", "zèbre"
    ]
    for key in to_add_keys_list:
        trie.add(key)

    others_keys = ["Bonjour", "Aurevoir", "Pomme"]
    
    for key in others_keys:
        print(f"L'arbre trie contient le mot {key}: {trie.contains(key)}")
    for key in to_add_keys_list:
        print(f"L'arbre trie contient le mot {key}: {trie.contains(key)}")
