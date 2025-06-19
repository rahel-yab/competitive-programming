# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def same(a, b):
            c = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    c += 1
            return c == 2 or c == 0

        def dfs(i):
            visited.add(i)
            for j in range(len(strs)):
                if j not in visited and same(strs[i], strs[j]):
                    dfs(j)

        visited = set()
        group = 0
        for i in range(len(strs)):
            if i not in visited:
                dfs(i)
                group += 1
        return group
