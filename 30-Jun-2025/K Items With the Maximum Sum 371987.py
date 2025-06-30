# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k
        elif numOnes + numZeros >= k:
            return numOnes
        elif numOnes + numZeros < k:
            return numOnes - (k-(numOnes+ numZeros))