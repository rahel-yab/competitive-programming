# Problem: Longest Mountain in Array - https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxx = 0
        ind = 1
        n = len(arr)
        while ind < n -1:
            if arr[ind] > arr[ind+1] and arr[ind-1] < arr[ind]:
                left = ind -1
                right = ind + 1
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < n-1 and arr[right+1] < arr[right]:
                    right += 1
                maxx = max(maxx , right -left + 1)
                ind = right
            else:
                ind += 1

        return maxx