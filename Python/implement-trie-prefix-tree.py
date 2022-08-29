#submitted 25/07/2022

class TrieNode:
    def __init__(self):
        self.isEnd = False;
        self.things = {}       

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        thing = self.root
        for c in word:
            if c not in thing.things:
                thing.things[c] = TrieNode()
            thing = thing.things[c]
        thing.isEnd = True
        
    def search(self, word: str) -> bool:
        thing = self.root
        for c in word:
            if c not in thing.things:
                return False
            thing = thing.things[c]
        return thing.isEnd

    def startsWith(self, prefix: str) -> bool:
        thing = self.root
        for c in prefix:
            if c not in thing.things:
                return False
            thing = thing.things[c]
        return True