# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ans  , curr = set() , []
        def backtrack(i):

            if len(curr) >= 2:
                ans.add(tuple(curr[:]))

            for j in range(i, len(nums)):
                if not curr or nums[j] >= curr[-1]:
                    curr.append(nums[j])
                    backtrack(j+1) 
                    curr.pop()
            
        for i in range(len(nums)):
            backtrack(i)
        
        return [list(sub) for sub in ans]