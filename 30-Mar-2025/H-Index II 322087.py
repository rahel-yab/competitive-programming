# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def validate(k):
            count = 0
            for citation in citations:
                if citation >= k:
                    count += 1
            
            return count >= k


        low = 0
        high = max(citations)
        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high