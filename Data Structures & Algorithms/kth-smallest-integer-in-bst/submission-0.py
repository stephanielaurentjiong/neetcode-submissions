# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # have smallest value

        # Start from the root
        # Have a stack

        # Keep going to the left (while loop)
        # Add Node to the stack until find a null node

        # Another loop to pop the node from the stack
        # Decrement the k
        # Continue pop and decrement until k == 0

        # If so, return the current poped node

        current = root
        stack = []

        while stack or current:

            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            k -= 1
            if (k == 0):
                return current.val

            current = current.right