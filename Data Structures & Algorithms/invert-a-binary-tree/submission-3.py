# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If there is no root, just return empty []
        if not root:
            return None

        # If there is no children, just return root
        if not root.left and not root.right:
            return root
        
        
        leftNode = self.invertTree(root.left)
        rightNode = self.invertTree(root.right)

        root.left, root.right = rightNode, leftNode
        
        return root

        
        

