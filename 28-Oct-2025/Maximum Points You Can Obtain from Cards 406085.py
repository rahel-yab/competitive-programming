# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        left = 0
        right = n -k -1
        curr_sum = sum(cardPoints[left:right+1])
        ans = max(0 , total-curr_sum)
        while right < n-1:
            curr_sum -= cardPoints[left]
            left += 1
            right += 1
            curr_sum += cardPoints[right]
            ans = max(ans , total - curr_sum)
        return ans
    
