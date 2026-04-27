# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Solution 1: DFS tracking max number up until top of stack
        stack = [(root, root.val)]
        count = 0

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
            if node.left:
                stack.append((node.left, max(max_val, node.left.val)))
            if node.right:
                stack.append((node.right, max(max_val, node.right.val)))

        return count