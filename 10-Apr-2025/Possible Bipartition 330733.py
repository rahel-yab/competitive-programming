# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n+1)]
        dis = [-1 for _ in range(n+1)]
        for u ,v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node,color):
            dis[node] = color
            for neigh in adj_list[node]:
                if dis[neigh] == -1:
                    if dfs(neigh, 1-color) == False:
                        return False
                elif dis[neigh] == color:
                    return False
            return True

        for i in range(1,n+1):
            if dis[i] == -1:
                if dfs(i,0) == False:
                    return False
        return True