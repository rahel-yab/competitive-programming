# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        def combination(k):
            if k < 0:
                return 0

            return (k+1)*(k+2)//2

        total = combination(n)
        one = 3 * combination(n - limit - 1)
        two = 3 * combination(n - 2 * limit - 2)
        three = combination(n - 3 * limit - 3)
        return total - one + two - three
