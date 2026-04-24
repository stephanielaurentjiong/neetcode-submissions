# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Preorder traversal 
        # Root -> left -> right
        # Used to know where the root

        # In order traversal
        # Left -> root -> right
        # Used to know the relative order of left and right node

        # Recursive
        # BC
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # Build the left node of the root
        root.left = self.buildTree(preorder[1:mid + 1], inorder[: mid])
        # Build the right node of the root
        root.right= self.buildTree(preorder[mid + 1:], inorder[mid + 1: ])
        return root
