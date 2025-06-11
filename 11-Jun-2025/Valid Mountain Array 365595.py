# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        peak = 0
        val = arr[0]
        inc = True
        for i in range(1, len(arr)):
            if arr[i] == val: 
                return False
            if i == 1 and arr[i] < val:
                return False

            if arr[i] < val and inc:
                peak += 1
                inc = False
            if arr[i] > val and not inc:
                return False 
            val = arr[i]

        return peak == 1
