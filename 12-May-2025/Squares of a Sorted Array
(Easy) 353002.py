# Problem: Squares of a Sorted Array
(Easy) - https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        res=[]
        
        while left<=right:
            if abs(nums[left])<abs(nums[right]):
                res.append(nums[right]**2)
                right-=1
            else:
                res.append(nums[left]**2)
                left+=1

        res.reverse()
        
        return res

        