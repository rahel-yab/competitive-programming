# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        s = set()
        n = len(nums)
        
        def backtrack():
            if len(arr) == n:
                ans.append(arr[:])
                return 

            for i in nums:
                if i in s:
                    continue
                arr.append(i)
                s.add(i)
                backtrack()
                arr.pop()
                s.remove(i)
        
        backtrack()
        return ans
