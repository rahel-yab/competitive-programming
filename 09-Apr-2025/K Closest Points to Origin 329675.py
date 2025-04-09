# Problem: K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minn = float('inf')
        ans = []
        res = []
        for u,v in points:
            dist = u**2 + v**2
            ans.append([dist,[u,v]])
        ans.sort()
        for i in range(k):
            res.append(ans[i][1])
        return res