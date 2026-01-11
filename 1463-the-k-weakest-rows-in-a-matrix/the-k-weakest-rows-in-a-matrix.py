class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        i = 0
        for row in mat:
            ans.append((i , sum(row)))
            i += 1

        ans.sort(key=lambda x : x[1])
        res = [i for i , j in ans]
        return res[:k]