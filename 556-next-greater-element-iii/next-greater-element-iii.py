class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, str(n)))
        l = len(nums)
    
        i = l - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1

        j = l - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1:] = reversed(nums[i + 1:])
        next_n = int(''.join(map(str, nums)))
        return next_n if next_n < 2**31 else -1