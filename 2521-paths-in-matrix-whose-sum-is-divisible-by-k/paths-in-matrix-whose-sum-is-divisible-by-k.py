class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        mod = 10**9 + 7
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        val = (grid[0][0] % k)
        dp[0][0][val] = 1
        for r in range(m):
            for c in range(n):
                for prev in range(k):
                    ways = 0
                    if r > 0:
                        ways = (ways + dp[r-1][c][prev])%mod
                    if c > 0:
                        ways = (ways+dp[r][c-1][prev])%mod
                    
                    curr = (prev + grid[r][c])%k 
                    dp[r][c][curr] = (dp[r][c][curr] + ways)%mod
            
        return dp[-1][-1][0]


