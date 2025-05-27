# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = float('-inf')
        n = len(arr)
        res = [0] * (n-1)
        for i in range(n-1,0,-1):
            maxx = max(maxx,arr[i])
            res[i-1] = maxx
        res.append(-1)
        return res