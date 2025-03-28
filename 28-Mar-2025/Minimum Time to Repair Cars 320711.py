# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def validate(time):
            n = 0
            for r in ranks:
                n += int((time//r) ** 0.5)
            return n >= cars

        low = 1
        high = 2 ** 50
        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                high = mid -1
            else:
                low = mid + 1
        return low