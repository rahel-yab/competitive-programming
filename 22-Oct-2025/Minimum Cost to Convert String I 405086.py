# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [[float("inf")] * 26 for _ in range(26)]

        for i in range(26):
            dist[i][i] = 0
        
        for i in range(len(cost)):
            u , v = ord(original[i]) - 97 , ord(changed[i]) - 97
            dist[u][v] = min(dist[u][v] , cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        ans = 0
        for i in range(len(source)):
            s ,c = ord(source[i])-97 , ord(target[i]) -97
            if s == c:
                continue
            if dist[s][c] == float("inf"):
                return -1
            ans += dist[s][c]
        
        return ans

