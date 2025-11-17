# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        n = len(graph) 
        def dfs(node , curr):
            curr.append(node)
            if node == n-1:
                paths.append(curr[:])
            else:
                for nei in graph[node]:
                    dfs(nei , curr)
                
            curr.pop()
            
        dfs(0 , [])
        return paths
