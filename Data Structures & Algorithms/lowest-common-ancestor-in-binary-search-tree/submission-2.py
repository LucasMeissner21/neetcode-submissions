# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iterative: binary search tree structure: left < current < right, so traverse tree
        # accordingly
        res = TreeNode(float('inf'))
        
        while True:
            if p.val < root.val and q.val < root.val: # Both values in left subtree
                root = root.left
            elif p.val > root.val and q.val > root.val: # Both values in right subtree
                root = root.right
            else: # If the current node is p or q, or one is right and one is left, current
                  # has to be the LCA
                return root

                