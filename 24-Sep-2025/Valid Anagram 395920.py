# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = Counter(s)
        count2 = Counter(t)
        for key , val in count1.items():
            if key not in count2 or count2[key] != val:
                return False
        for key , val in count2.items():
            if key not in count1 or count1[key] != val:
                return False
        
        return True