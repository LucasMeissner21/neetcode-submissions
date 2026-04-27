# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Solution 1: Iterative BFS, return false if BST rule broken
        stack = [(root, float("-inf"), float("inf"))]

        while stack:
            node, left, right = stack.pop(0)
            if not (left < node.val < right):
                return False
            if node.left: # Left nodes have to be less than parent's value
                stack.append((node.left, left, node.val))
            if node.right: # Right nodes have to be greater than parent's value
                stack.append((node.right, node.val, right))

        return True