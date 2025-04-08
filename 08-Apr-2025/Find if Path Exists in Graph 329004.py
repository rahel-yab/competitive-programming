# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        visited = set()
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfs(edge, visited):
            if edge == destination:
                return True
            
            visited.add(edge)
            for neigh in adj_list[edge]:
                if neigh not in visited:
                    found = dfs(neigh, visited)
                    if found:
                        return True
            return False
        return dfs(source, visited)