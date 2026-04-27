# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Second Attempt, serialize the root and subroot then check if subroot is in root
        root_s = ""
        subRoot_s = ""

        root_s = self.serialize(root)
        subRoot_s = self.serialize(subRoot)

        if root_s == subRoot_s:
            return True

        n = len(subRoot_s)

        for i in range(len(root_s) - n + 1):
            if root_s[i:i + n] == subRoot_s:
                return True
        return False

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        
        return f"${root.val}{self.serialize(root.left)}{self.serialize(root.right)}"

