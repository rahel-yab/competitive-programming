# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = [arr[0]]
        for i in range(1,len(arr)):
            res.append(res[i-1] ^ arr[i])
        
        ans = []
        for left,right in queries:
            if left == 0:
                ans.append(res[right])
            else:
                val = res[right] ^ res[left-1]
                ans.append(val)
        return ans
