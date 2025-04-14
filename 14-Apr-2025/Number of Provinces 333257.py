# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neigh in range(n):
                if isConnected[node][neigh] == 1 and neigh not in visited:
                    dfs(neigh)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
