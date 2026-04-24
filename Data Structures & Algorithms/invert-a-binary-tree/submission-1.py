# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Edge case: check if input/tree is empty
        if root is None:
            return None
        
        #Swap the left and right node
        root.left, root.right = root.right, root.left

        #Recursively do the swapping on the subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        