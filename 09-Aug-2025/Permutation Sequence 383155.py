# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = []
        count = 0
        ans = ""
        
        def backtrack(curr):
            nonlocal count, ans
            if len(arr) == n:
                count += 1
                if count == k:
                    ans = ''.join(str(i) for i in arr)
                return
            if ans: 
                return
            for i in range(1, n + 1):
                if i in curr:
                    continue
                curr.add(i)
                arr.append(i)
                backtrack(curr)
                curr.remove(i)
                arr.pop()

        backtrack(set())
        return ans