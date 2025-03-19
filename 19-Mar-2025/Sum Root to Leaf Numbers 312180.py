# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        summ = 0
        def helper(node, nums):
            nonlocal summ
            if node == None:
                return 
            nums += str(node.val)
            if not node.left and not node.right:
                summ += int(nums) 
                return
            if node.left:
                helper(node.left, nums)
            if node.right:
                helper(node.right, nums)
        
        helper(root, "")
        return summ