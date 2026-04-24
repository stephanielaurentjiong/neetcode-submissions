# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        
        if not p and not q:
            return True
            
        # If one is none, the other is not
        if not p and q:
            return False
        if not q and p:
            return False

            # Check if p and q has the same value
        if p.val != q .val:
            return False
            
        # Return boolean
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        
        return False
            
          

