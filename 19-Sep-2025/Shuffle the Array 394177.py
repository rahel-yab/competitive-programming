# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        ans = []
        while right < 2*n:
            ans.append(nums[left])
            ans.append(nums[right])
            left += 1
            right += 1
        
        return ans