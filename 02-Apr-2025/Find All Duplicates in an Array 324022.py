# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        count = Counter(nums)
        for num in count:
            if count[num] == 2:
                res.append(num)
        return res
        