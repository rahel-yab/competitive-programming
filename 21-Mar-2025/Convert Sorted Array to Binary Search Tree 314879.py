# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sorted(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = sorted(nums[:mid])
            new_node.right = sorted(nums[mid+1:])
            return new_node
        return sorted(nums)

            