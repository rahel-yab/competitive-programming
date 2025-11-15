# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxx = 0
        def dfs(root, length):
            nonlocal maxx
            if not root:
                return 0
            
            for child in root.children:
                dfs(child, length+1)
            
            maxx = max(maxx , length)
            return maxx

        return dfs(root , 1)    