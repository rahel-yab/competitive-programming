# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        eq = []
        greater = []
        for i in nums:
            if i < pivot:
                less.append(i)
        for i in nums:
            if i == pivot:
                eq.append(i)
        for i in nums:
            if i > pivot:
                greater.append(i)
        if eq:
            return less + eq+ greater
        return less + greater