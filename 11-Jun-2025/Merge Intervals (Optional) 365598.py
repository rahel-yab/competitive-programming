# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        res = []
        intervals.sort()
        res.append(intervals[0])
        for i in range(len(intervals)-1):
            x,y = res[-1]
            z,w = intervals[i+1]
            if y >= z:
                res[-1] = [x,max(y,w)]
            else:
                res.append(intervals[i+1])
        return res
