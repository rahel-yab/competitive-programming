# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(query: str, pattern: str) -> bool:
            i = j = 0
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    return False
                i += 1
            return j == len(pattern)

        return [check(query, pattern) for query in queries]