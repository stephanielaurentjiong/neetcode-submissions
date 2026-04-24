# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q :
            return True
        
        # Check the node
        if p and not q:
            return False
        if not p and q:
            return False
        
        # Checks the value
        if p.val != q.val:
            return False
        
        boolean_left = self.isSameTree(p.left, q.left)
        boolean_right = self.isSameTree(p.right, q.right)

        return boolean_left and boolean_right
        