# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
    
        def dfs(root):
            if not root:
                return (0, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            return (root.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))
        

        return max(dfs(root))