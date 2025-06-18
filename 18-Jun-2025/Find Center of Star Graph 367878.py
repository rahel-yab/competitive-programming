# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for i in range(n+1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(1,n+1):
            if len(graph[i]) == n -1:
                return i

