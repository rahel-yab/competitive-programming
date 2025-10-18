# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            flag = False
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    ans.append(nums[j])
                    flag = True
                    break
            if flag:
                continue
            for j in range(i):
                if nums[j] > nums[i]:
                    ans.append(nums[j])
                    flag = True
                    break
                if flag:
                    continue
            if not flag:
                ans.append(-1)
        
        return ans
                