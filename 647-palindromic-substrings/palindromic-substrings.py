class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        def check(left, right):
            state = (left , right)
            if state in memo:
                return memo[state]

            if left > right:
                return True
            
            if s[left] == s[right]:
                memo[state] = check(left+1, right-1)
                return memo[state]
            
            return False
        
        ans = 0
        for i in range(len(s)):
            for j in range(i , len(s)):
                if check(i , j):
                    ans += 1
        
        return ans
