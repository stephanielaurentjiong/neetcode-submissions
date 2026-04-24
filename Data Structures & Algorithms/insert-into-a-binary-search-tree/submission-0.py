# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Do a search on the BST
        #If the root is None --> create a Treenode with the given value
        #Otherwise, use recursion to search down the tree
            #Check if the current root is greater than or equal to the inserted target
                #Go to the right subtree
            #Otherwise
                #Go to the left subtree
        
        if not root:
            return TreeNode(val)

        if root.val < val:
            print(f" root.right {root.right}")
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root