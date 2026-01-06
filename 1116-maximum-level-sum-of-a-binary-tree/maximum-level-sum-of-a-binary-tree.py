# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root , 1))
        maxx = float("-inf")
        ans = 0
        while q:
            curr_sum = 0
            size = len(q)
            for _ in range(size):
                node , level = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append((node.left , level +1))
                if node.right:
                    q.append((node.right , level+1))
            if curr_sum > maxx:
                maxx = curr_sum
                ans = level
        
        return ans
        



