class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1 , n+1):
            for j in range(1 , n+1):
                if ((i**2 + j**2))**0.5 == math.isqrt((i**2 + j**2)) and ((i**2 + j**2))**0.5 <= n:
                    ans += 1

        return ans
