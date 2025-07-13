# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count = Counter(t)
        count2 = Counter()
        left = 0
        start = 0
        minn = float('inf')
        curr = 0
        ans = len(count)

        for right in range(len(s)):
            char = s[right]
            count2[char] += 1

            if char in count and count2[char] == count[char]:
                curr += 1

            while curr == ans:
                if right - left + 1 < minn:
                    minn = right - left + 1
                    start = left
                count2[s[left]] -= 1
                if s[left] in count and count2[s[left]] < count[s[left]]:
                    curr -= 1
                left += 1
        if minn == float('inf'):
            return ""
        else:
            return s[start:start + minn]