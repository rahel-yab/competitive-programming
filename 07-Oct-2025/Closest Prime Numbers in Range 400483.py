# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive = [True] * (right+1)
        
        seive[0] = False
        seive[1] = False

        for i in range(2,right+1):
            if seive[i]:
                for j in range(i*i , right+1 , i):
                    seive[j] = False
        primes = []
        for num in range(2,right+1):
            if seive[num] and num >= left:
                primes.append(num)
        left = 0
        right = 1
        minn = float("inf")
        ans = [-1, -1]
        while right < len(primes):
            diff = primes[right] - primes[left]
            if diff < minn:
                minn = diff
                ans = [primes[left] , primes[right]]
            left += 1
            right += 1
        return ans