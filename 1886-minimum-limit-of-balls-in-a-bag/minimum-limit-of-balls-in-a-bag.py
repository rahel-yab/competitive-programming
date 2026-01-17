class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def validate(mid):
            curr = sorted(nums)
            c = 0
            while curr and curr[-1] > mid:
                c += ceil(curr[-1] / mid) - 1
                curr.pop()

            return c <= maxOperations

        low , high = 1 , max(nums)
        while low <= high:
            mid = (low+high) // 2
            if validate(mid):
                high = mid -1
            else:
                low = mid + 1
        
        return low