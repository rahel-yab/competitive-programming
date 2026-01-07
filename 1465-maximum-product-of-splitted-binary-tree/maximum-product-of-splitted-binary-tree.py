# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        curr = []
        def dfs(node):
            nonlocal total
            if not node:
                return 
            
            total = node.val 
            if node.left:
                total += dfs(node.left) 
            if node.right:
                total += dfs(node.right)
            # print(total)
            curr.append(total)
            return total

        total = dfs(root)
        maxx = float("-inf")
        for num in curr:
            maxx = max(maxx , (total-num) * num)
        return maxx % (10**9 + 7)