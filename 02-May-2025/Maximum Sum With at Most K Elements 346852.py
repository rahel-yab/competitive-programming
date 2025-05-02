# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        maxi= []
        for i in range(len(grid)):
            heap = []
            for j in grid[i]:
                heapq.heappush(heap, j)
            maxi.extend(heapq.nlargest(limits[i], heap))
        heapq.heapify(maxi)
        maxi.sort(reverse=True)
        return sum(maxi[:k])