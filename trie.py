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
        return bool(self.extensions)
    
    def leaf(self, key:str) -> _Node:
        if self.is_leaf():
            return self
        return self.extensions[key[0]].get_leaf(key[1:])

    def contained_part_split(self, key:str, index:int=1) -> tuple[str, str]:
        if not self.contains(key[:index]):
            return key[:index-1], key[index-1:]
        return self.contained_part_split(key, index + 1)
    
    def __str__(self) -> str:
        return f"|__{self.value }\n"


class Trie:
    def __init__(self) -> None:
        self.head = _Node("")

    def contains(self, key:str) -> bool: 
        return self.head.contains(key)

    def add(self, key:str) -> None:
        if not self.head.contains(key):
            contained_part, new_part = self.head.contained_part_split(key)
            self.head.leaf(contained_part).extend(new_part)
