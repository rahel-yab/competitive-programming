# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        res = []
        for i in range(int(math.sqrt(c)+1)):
            res.append(i)

        left = 0
        right = len(res)-1

        while left < right:

            if res[left]**2 + res[right]**2 == c or res[left]**2+ res[left]**2 == c or res[right]**2 + res[right]**2 == c:
                return True

            elif res[left]**2+ res[right]**2 >c:
                right -= 1

            else:
                left += 1

        return False
            

        
        