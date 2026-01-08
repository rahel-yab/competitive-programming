class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(i , j):
            if i >= len(nums1) or j >= len(nums2):
                return float("-inf")
            
            return max(nums1[i] * nums2[j] + max(0 ,dp(i+1,j+1)) ,
            dp(i , j+1),
            dp(i+1 , j+1),
            dp(i+1 , j))
        
        return dp(0 , 0)