# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node , i):
            if i == len(word):
                return node.end  
            if word[i] == '.':
                for chi in node.children.values():
                    if dfs(chi,i+1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]] , i+1)
            return False
        return dfs(self.root , 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)