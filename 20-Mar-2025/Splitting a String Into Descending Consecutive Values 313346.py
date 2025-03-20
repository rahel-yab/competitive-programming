# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        curr = []
        def backtrack(index):
            if index >= len(s):
                for i in range(1,len(curr)):
                    if curr[i-1] - curr[i] != 1:
                        return False
                return len(curr) >= 2

            for ind in range(index,len(s)):
                val = int(s[index:ind +1])
                if curr:
                    if curr[-1] - val != 1:
                        continue
                curr.append(val)
                if backtrack(ind+1):
                    return True
                curr.pop()
            return False
        return backtrack(0)
    
