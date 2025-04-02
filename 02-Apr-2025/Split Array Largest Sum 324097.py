# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def validate(mid):
            summ = 0
            group = 1
            for num in nums:
                if num + summ <= mid:
                    summ += num
                else:
                    group += 1
                    summ = num
            return group <= k
        

        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low+ high)//2
            if validate(mid):
                high = mid -1
            else:
                low = mid + 1
        return low