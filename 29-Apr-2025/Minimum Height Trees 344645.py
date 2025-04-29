# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indeg = [0 for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indeg[u] += 1
            graph[v].append(u)
            indeg[v] += 1
        
        q = deque()
        for i in graph:
            if indeg[i] == 1:
                q.append(i)
        while q:
            if n <= 2:
                return list(q)
            for i in range(len(q)):
                node = q.popleft()
                n -= 1
                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 1:
                        q.append(nei)
                    

            
