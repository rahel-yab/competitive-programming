# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ans = [-1,-1]
        for i in range(n):
            for j in range(n):
                if abs(i-j) >= indexDifference:
                    if abs(nums[i] - nums[j]) >= valueDifference:
                        ans = [i,j]
                        break
        return ans
