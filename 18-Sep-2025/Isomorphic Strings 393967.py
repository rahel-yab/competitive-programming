# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapp = defaultdict()
        mapp2 = defaultdict()
        for i in range(len(s)):
            if t[i] in mapp2 and mapp2[t[i]] != s[i]:
                return False
            if s[i] in mapp and mapp[s[i]] != t[i]:
                return False
            mapp[s[i]]= t[i]
            mapp2[t[i]] = s[i]
        
        return True