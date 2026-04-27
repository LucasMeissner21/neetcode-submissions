# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Solution 1: Morris traversal to build tree using preorder and matching to inorder

        start = TreeNode(None) # Dummy
        curr = start
        i, j, n = 0, 0, len(preorder) # i tracks preorder values and j tracks inorder

        while i < n and j < n:
            # Create node to the right linking to itself
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            # Link back up to parent until all preorder values have been added or predecessor
            # found
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right = curr) 
                curr = curr.left
                i += 1
            j += 1
            # Unlink until no more right values, all in order have been added, or until all
            # have been unlinked (Going back up tree while doing so)
            while curr.right and j < n and curr.right.val == inorder[j]: 
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return start.right