# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        ind = [i for i in range(n) if s[i].isalpha()]
        c = len(ind)
        res = []
        for i in range(2**c):
            curr = list(s)
            for j in range(c):
                if (i & (1 << j)):
                    curr[ind[j]] = curr[ind[j]].upper()
                else:
                    curr[ind[j]] = curr[ind[j]].lower()
                    
            res.append(''.join(curr))
        return res