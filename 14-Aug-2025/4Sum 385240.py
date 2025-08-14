# Problem: 4Sum - https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        start1 = 0
        while start1 < n - 3:
            if start1 > 0 and nums[start1] == nums[start1 - 1]:
                start1 += 1
                continue

            start2 = start1 + 1
            while start2 < n - 2:
                if start2 > start1 + 1 and nums[start2] == nums[start2 - 1]:
                    start2 += 1
                    continue

                left = start2 + 1
                right = n - 1
                while left < right:
                    summ = nums[start1] + nums[start2] + nums[left] + nums[right]
                    if summ == target:
                        ans.append([nums[start1], nums[start2], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif summ < target:
                        left += 1
                    else:
                        right -= 1

                start2 += 1
            start1 += 1
    
        return ans