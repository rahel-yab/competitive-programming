# Problem: Kids With the Greatest Number of Candies - https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        ans = [False for _ in range(len(candies))]
        for i ,candy in enumerate(candies):
            curr = candy + extraCandies
            if curr >= maxx:
                ans[i] = True
        return ans