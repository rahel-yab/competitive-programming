# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:  
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:  
        n = len(nums)
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        ans = []
        for val , ind in queries:
            curr = nums[ind] + val
            if curr % 2 == 0:
                even_sum += curr
            if nums[ind] % 2 == 0:
                even_sum -= nums[ind]

            nums[ind] = curr
            ans.append(even_sum)
        
        return ans
        