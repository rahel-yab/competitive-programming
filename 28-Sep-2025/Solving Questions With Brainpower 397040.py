# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]

            if i >= len(questions):
                return 0
            
            skip = dp(i+1)
            solve = questions[i][0] + dp(i+1+questions[i][1])
            memo[i] = max(skip,solve)
            return memo[i]
    
        return dp(0)