# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        ans = 0
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        def dfs(edge, comp):
            visited.add(edge)
            comp.append(edge)
            for neigh in adj_list[edge]:
                if neigh not in visited:
                    dfs(neigh,comp)
        def complete(comp):
            s = len(comp)
            for i in comp:
                if len(adj_list[i]) != s-1:
                    return False
            return True

        for i in range(n):
            if i not in visited:
                comp = []
                dfs(i,comp)
                if complete(comp):
                    ans += 1
        return ans