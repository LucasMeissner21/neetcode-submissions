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
            # Creates new node to the right after landing at next inorder, keeping previous link 
            # to parent above
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            # Add nodes to the left linking with parent to the right until all nodes are added
            # or current inorder node is found (left-most unproccessed node), left spine
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right = curr) 
                curr = curr.left
                i += 1
            j += 1
            # Traverse back up the spine just created until next value inorder isn't the parent,
            # means right subtree must be added. Snip connections to parent as we go
            while curr.right and j < n and curr.right.val == inorder[j]: 
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return start.right