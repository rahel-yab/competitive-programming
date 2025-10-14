# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        class TrieNode:
            def __init__(self):
                self.children = [None] * 26
                self.end = False

        class Trie:
            def __init__(self):
                self.root = TrieNode()

            def add(self, word):
                curr = self.root
                for ch in word:
                    idx = ord(ch) - ord('a')
                    if curr.children[idx] is None:
                        curr.children[idx] = TrieNode()
                    curr = curr.children[idx]
                curr.end = True

            def prefix(self, word):
                curr = self.root
                for ch in word:
                    idx = ord(ch) - ord('a')
                    curr = curr.children[idx]
                    if curr is None or not curr.end:
                        return False
                return True

        t = Trie()
        for w in words:
            t.add(w)

        ans = ""
        for w in words:
            if t.prefix(w):
                if len(w) > len(ans) or (len(w) == len(ans) and w < ans):
                    ans = w
        return ans