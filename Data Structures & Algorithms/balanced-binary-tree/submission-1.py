# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        diff = 0
        def dfs(root):
            
            if not root:
                return 0

            #Visit the first node
            #Take the left child 
            left_depth = dfs(root.left) 
            #Take the right child
            right_depth = dfs(root.right) 

            if left_depth == -1:
                return -1
            if right_depth == -1:
                return -1
            # If at that root, the left and right subtree is already unbalanced, return -1
            if abs(left_depth - right_depth) > 1:
                return -1
            # Otherwise, choose which subtree has the longest path + 1
            return 1 + max(left_depth, right_depth)

        return dfs(root) != -1
