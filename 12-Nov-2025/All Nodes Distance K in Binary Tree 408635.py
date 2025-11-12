# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def change(root):
            if not root:
                return 
            parent = root.val
            if root.left:
                graph[root.left.val].append(parent)
                graph[parent].append(root.left.val)
                change(root.left)
            if root.right:
                graph[root.right.val].append(parent)
                graph[parent].append(root.right.val)
                change(root.right)
        
        change(root)
        ans = []
        q = deque()
        q.append((target.val , 0))
        visited = set()
        visited.add(target.val)
        while q:
            node , dist = q.popleft()
            if dist == k:
                ans.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    q.append((nei , dist+1))
                    visited.add(nei)
        
        
        return ans
  

        