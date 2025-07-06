# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        heap = []
        for u, v in intervals:
            if heap and heap[0] < u:
                heapq.heapreplace(heap, v)
            else:
                heapq.heappush(heap, v)
        return len(heap)
