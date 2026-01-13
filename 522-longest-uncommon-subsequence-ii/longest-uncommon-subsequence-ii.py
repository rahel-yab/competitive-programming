class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(a , b):
            i = 0
            for ch in b:
                if i < len(a) and a[i] == ch:
                    i += 1
            return i == len(a)
        
        strs.sort(key=lambda x : -len(x))

        for i , s in enumerate(strs):
            if all(not check(s , strs[j]) for j in range(len(strs)) if j != i):
                return len(s)
        
        return -1