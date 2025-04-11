# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [[] for _ in range(n)]
        for u, v in edges:
            indeg[v].append(u)
        
        count = 0
        champ = None
        for i in range(n):
            if indeg[i] == []:
                count += 1
                champ = i
        if count == 1:
            return champ
        else:
            return -1