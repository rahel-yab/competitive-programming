# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def dp(turn, left, right):
            state = (turn, left, right)
            if state in memo:
                return memo[state]

            if left == right:
                return 0
            
            alice , bob = 0, 0

            if turn % 2 == 0 and piles[left] > piles[right]:
                alice = piles[left] + dp(turn+1, left+1, right)
            elif turn % 2 == 0 and piles[left] <= piles[right]:
                alice = piles[right] + dp(turn+1, left, right-1)

            if turn % 2 == 1 and piles[left] > piles[right]:
                bob = piles[left] + dp(turn+1, left+1, right)
            elif turn % 2 == 1 and piles[left] <= piles[right]:
                bob = piles[right] + dp(turn+1, left, right-1)
            
            memo[state] = alice > bob
            return memo[state]
        
        return dp(0,0, len(piles)-1)
            

