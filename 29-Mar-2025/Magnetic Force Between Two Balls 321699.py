# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def validate(k):
            pre = position[0]
            diff = 1
            for i in range(1,len(position)):
                if position[i] - pre >= k:
                    diff += 1
                    pre = position[i]
            return diff >= m
        
        position.sort()
        low = 1
        high = max(position) - min(position)
        while low <= high:
            mid = (low+ high)//2
            if validate(mid):
                low = mid + 1
            else:
                high = mid -1
            
        return high