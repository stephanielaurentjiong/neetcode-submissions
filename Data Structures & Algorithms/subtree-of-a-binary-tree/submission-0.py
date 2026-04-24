# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If not subRoot, either root is null or non-null is true
        if not subRoot:
            return True
        if not root: 
            return False

        if self.sameTree(root, subRoot):
            return True
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # A null subtree is a SUBTREE of a null tree
        if not root and not subRoot:
            return True
            # But if not a null subtree and null tree
            # Check if
            #  1. Root is not null
            #  2. The subroot is not nnull
            #  3. the value of the current root the same
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))
        return False

