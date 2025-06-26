# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for w in strs:
            curr = ''.join(sorted(w))
            dictt[curr].append(w)

        return list(dictt.values())





        