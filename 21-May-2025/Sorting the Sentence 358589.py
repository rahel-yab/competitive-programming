# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        res = [i for i in s.split()]
        ans = [0] * len(res)
        for word in res:
            ind = int(word[-1])
            ans[ind-1] = word[:len(word)-1]
        # print(ans)
        return ' '.join(ans)