# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        black = 0
        
        for c in s:
            if c == "0":
                swap += black
            else:
                black += 1

        return swap

        