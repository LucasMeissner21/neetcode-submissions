# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Solution 3: Morris Traversal (traversal in order with O(1) extra space)

        curr = root
        while curr:
            if not curr.left: # No predecessor exists, dec k
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right # Step to the right

            else:
                pred = curr.left
                # Find predecessor of current node
                while pred.right and pred.right != curr:
                    pred = pred.right

                # If predecessor hasn't been found, link to current and step left
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                # If predecessor has already been linked, unlink and dec k, next kth smallest
                # has been found, then step right to get next smallest
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        
        return -1 # Error
