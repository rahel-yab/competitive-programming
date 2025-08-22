# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for i in range(len(equations)):
            u , v = equations[i]
            graph[u].append([values[i],v])
            graph[v].append([1/values[i] , u])
        

        def dfs(x,y, visited):
            if x not in graph or y not in graph:
                return -1
            if x == y:
                return 1
            
            visited.add(x)
            for val , nei in graph[x]:
                if nei not in visited:
                    res = dfs(nei,y,visited)
                    if res != -1:
                        return res * val               
                
            return -1


        ans = []
        for x , y in queries: 
            ans.append(dfs(x,y,set()))
        return ans




        