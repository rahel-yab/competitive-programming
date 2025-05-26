# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        
        count = Counter(deck)
        vals = list(count.values())
        gcd = vals[0]
        for v in vals[1:]:
            gcd = math.gcd(gcd, v)
        
        return gcd >= 2