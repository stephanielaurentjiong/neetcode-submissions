# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS -- FIFO
        # DS: deque

        # visited set to be returned
        # deque to line up the next node for processing

        # Add first node to visited and deque
        # Processing the node until no node to be processed left
            # Pop of the node from q
            # Check if q is already on visited, if not
                # add to visited
            # Else: continue
            # For each of this node's neighbor, add to visited and q
        if not root:
            return []
            
        result = []
        q = deque([root])
        while q:
            level_size = len(q)
            # For storing result for each level
            level = []
            for i in range(level_size):
                node = q.popleft()
             
                level.append(node.val)
                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
            result.append(level)
        
        return result
