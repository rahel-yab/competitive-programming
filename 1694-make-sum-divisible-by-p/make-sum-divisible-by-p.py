class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        dictt = {0:-1}

        summ = sum(nums)
        if summ%p == 0:
            return 0
        
        n = len(nums)
        pre = 0
        ans = n
        for i , num in enumerate(nums):
            pre = (pre+num)%p
            val = (pre-(summ % p )+ p) % p 
            if val in dictt:
                ans = min(ans , i - dictt[val])
            
            dictt[pre] = i
        
        return ans if ans != n else -1
