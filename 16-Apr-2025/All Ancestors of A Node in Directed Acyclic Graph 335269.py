# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        ans = [[] for _ in range(n)]
        
        for u, v in edges:
            adj_list[v].append(u)
        
        def dfs(node, curr, visited):
            visited.add(node)
            for parent in adj_list[node]:
                if parent not in curr:
                    curr.append(parent)
                    if parent not in visited:
                        dfs(parent, curr, visited)
        
        for i in range(n):
            curr = []
            visited = set()
            dfs(i, curr, visited)
            ans[i] = sorted(curr)
        
        return ans
