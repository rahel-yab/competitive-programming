# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def check(start, end):
            n = end - start + 1
            graph = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 2, n):
                    graph[i].append(j)

            memo = {}
            def dfs(i):
                if i in memo:
                    return memo[i]
                maxx = 0
                for nei in graph[i]:
                    maxx = max(maxx, dfs(nei))
                memo[i] = maxx + nums[start + i]
                return memo[i]

            return max(dfs(i) for i in range(n))

        if len(nums) == 1:
            return nums[0]
        return max(
            check(0, len(nums) - 2),
            check(1, len(nums) - 1)   
        )
