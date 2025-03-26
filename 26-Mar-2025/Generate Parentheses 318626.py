# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr , opens , close):
            if close > opens:
                return
            if len(curr) == 2*n:
                if opens == close:
                    res.append(''.join(curr))
                return
            
            for bracket in '()':
                curr.append(bracket)
                if bracket == '(':
                    opens +=  1
                else:
                    close += 1
            
                backtrack(curr, opens , close)
                curr.pop()
        
                if bracket == '(':
                    opens -=  1
                else:
                    close -= 1


        backtrack([], 0 , 0)
        return res

# test = Solution()
# print("here", test.generateParenthesis(8))

        