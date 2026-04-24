from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_len = 0


        def dfs(node):
            # Checks if a node is null, return the length
            if not node:
                return 0
            

            # Compute the depth of left and right subtrees
            left_d = dfs(node.left)
            right_d = dfs(node.right) 

            # Compute the longest path
            # update diameter: longest path passes through this node
            # left_d + right_d to count for paths from most left node to most right node
            self.max_len = max(self.max_len, left_d + right_d)

            # return the depth of the subtree rooted at this node
            return 1 + max(left_d, right_d)

        dfs(root)
        return self.max_len

        