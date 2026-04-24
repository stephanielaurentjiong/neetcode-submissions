# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True #Because if there is a root, but the subroot does not exists, it still valid tree
        if not root:
            return False #But if no root, but the subTree either has a root or no root, it is False


        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

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
        
        
