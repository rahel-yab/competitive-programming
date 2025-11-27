class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        nums = [i for i in range(n+1)]

        left = 0
        right = n
        ans = []
        i = 0
        while left <= right and i < n:
            if s[i] == 'I':
                ans.append(nums[left])
                left += 1
            else:
                ans.append(nums[right])
                right -= 1
            
            i+=1

        sett = set(ans)
        for num in range(n+1):
            if num not in sett:
                ans.append(num)
                break

        return ans
            




