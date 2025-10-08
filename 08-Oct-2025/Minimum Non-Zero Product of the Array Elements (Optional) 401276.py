# Problem: Minimum Non-Zero Product of the Array Elements (Optional) - https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        pr = 1000000007
        n = pow(2, p) - 1
        return (n * pow(n - 1, n // 2, pr)) % pr