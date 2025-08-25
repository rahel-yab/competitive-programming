# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        sett = set()
        def prime(n):
            while n % 2 == 0:
                sett.add(2)
                n //= 2
            
            for i in range(3, int(isqrt(n))+1):
                while n % i == 0:
                    n //= i
                    sett.add(i)
            
            if n >= 2:
                sett.add(n)
        
        for num in nums:
            prime(num)

        return len(sett)
