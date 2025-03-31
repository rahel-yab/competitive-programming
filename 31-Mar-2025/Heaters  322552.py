# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def validate(k):
            left = 0
            right = 0
            while left < len(houses) and right < len(heaters):
                if abs(heaters[right] - houses[left]) <= k:
                    left += 1
                else:
                    right += 1
            return left >= len(houses)
        

        low = 0
        high = 2 ** 40
        while low <= high:
            mid = (low+ high) //2
            if validate(mid):
                high = mid -1
            else:
                low = mid + 1
        return low