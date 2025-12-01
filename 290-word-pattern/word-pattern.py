class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(set(s)) != len(set(list(pattern))) or len(s)!= len(pattern):
            return False

        dictt = defaultdict(list)
        for i in range(len(pattern)):
            dictt[pattern[i]].append(s[i])
        
       
        for v in dictt.values():
            if len(set(v)) > 1:
                return False
        
        return True
