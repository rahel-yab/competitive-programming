# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def validate(candy):
            count = 0
            for c in candies:
                count += c // candy
            return count >= k



        low = 1
        high = max(candies)
        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                low = mid + 1
            else:
                high = mid -1
        
        if 0 <= high <= max(candies):
            return high
        else:
            return 0