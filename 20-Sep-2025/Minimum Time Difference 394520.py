# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def change(time):
            hour , minute = map(int, time.split(":"))
            return hour * 60 + minute
        
        minutes = [change(m) for m in timePoints]
        minutes.sort()
        minn = float('inf')
        for i in range(1,len(timePoints)):
            minn = min(minn , minutes[i] - minutes[i-1])
        
        val = 1440 - minutes[-1] + minutes[0]
        minn = min(minn , val)

        return minn