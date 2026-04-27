# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Solution 1: iterative BFS tracking each level and adding right most value
        if not root:
            return []
        res = []
        res.append(root.val)
        stack = []
        stack.append(root)

        while stack:
            level = []
            while stack: # Get next level from current level
                if stack[0].left:
                    level.append(stack[0].left)
                if stack[0].right:
                    level.append(stack[0].right)
                stack.pop(0)
            if level: # Add rightmost value to res
                res.append(level[len(level) - 1].val)
            stack = level
        
        return res
