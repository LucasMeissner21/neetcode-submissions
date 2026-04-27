# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # First Attempt, iterative BFS with recursive DFS check for equality at each node
        stack = []
        stack.append(root)
        # Iterative BFS
        while stack:
            if self.sameTree(stack[0], subRoot): # Recursive DFS function call
                return True
            left = stack[0].left
            right = stack[0].right
            if left:
                stack.append(left)
            if right:
                stack.append(right)
            stack.pop(0)
        return False

    # Recursive DFS function to check if trees are equal
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False 