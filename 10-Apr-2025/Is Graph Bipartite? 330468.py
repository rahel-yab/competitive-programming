# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for _ in range(n)]

        def dfs(node, curr):
            color[node] = curr
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - curr):
                        return False
                elif color[neighbor] == curr:
                    return False
            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False
        return True
