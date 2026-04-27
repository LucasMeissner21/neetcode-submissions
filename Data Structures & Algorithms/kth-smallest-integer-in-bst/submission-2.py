# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Solution 1: Iterative DFS, dec k after traversing as far left as possible
        # then go to the current node's right value, allows traversal from least to greatest
        stack = []
        curr = root

        while stack or curr:
            while curr: # Go as left as possible
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() # current kth smallest value
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right # Next smallest value
