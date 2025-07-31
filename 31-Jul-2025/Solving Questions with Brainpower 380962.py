# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n

        def check(j):
            if j >= n:
                return 0
            if dp[j]:
                return dp[j]

            p, b = questions[j]
            solve = p + check(j + b + 1)
            skip = check(j + 1)

            dp[j] = max(solve, skip)
            return dp[j]

        return check(0)