# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def validate(k):
            arr = [0] * (len(nums) + 1)
            for li , ri , val in queries[:k]:
                arr[li] += val
                arr[ri + 1] -= val
            prefix2 = [0] * (len(nums) + 1)
            prefix2[0] = arr[0]
            for i in range(1, len(nums)):
                prefix2[i] = prefix2[i-1] + arr[i]
            for i in range(len(nums)):
                if nums[i] - prefix2[i] > 0:
                    return False
            return True



        flag = False
        low = 0
        high = len(queries)
    
        while low <= high:
            mid = (low + high)//2
            print(validate(mid))
            if validate(mid):
                flag = True
                high = mid -1
            else:
                low = mid + 1
        if flag:
            return low
        else:
            return -1