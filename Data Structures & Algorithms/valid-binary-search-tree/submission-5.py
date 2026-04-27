# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Solution 2: Recursive DFS, return false if BST rule broken
        def checkValid(node: Optional[TreeNode], low : int, high : int) -> bool:
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            return checkValid(node.left, low, node.val) and checkValid(node.right, node.val, high)

        return checkValid(root, float("-inf"), float("inf"))
        