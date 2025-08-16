# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        s = s.split(' ')
        maxx = max(len(word) for word in s)
        for i in range(maxx):
            col = []
            for w in s:
                if i > len(w)-1:
                    col.append(' ')
                else:
                    col.append(w[i])
            print(col)
            ans.append(''.join(col).rstrip(' '))
        return ans
