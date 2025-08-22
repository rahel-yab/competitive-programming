# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def check(i):
            if not i:
                return 0
            nonlocal ans
            if i.left:
                ans += i.left.val
            if i.right:
                ans += i.right.val
            return ans 
        def dfs(i):
            if not i:
                return 0
            if i.val % 2 == 0:
                check(i.left)
                check(i.right)
            if i.left:
                dfs(i.left)
            if i.right:
                dfs(i.right)
                
        dfs(root)
        return ans
        
            

