# Problem: Delete Columns to Make Sorted - https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            res = []
            for j in range(len(strs)):
                res.append(strs[j][i])
            curr = sorted(res)
            if res != curr:
                count += 1
        return count
            
