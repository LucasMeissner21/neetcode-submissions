# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        res = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if not node:
                res.append("#")
            else:
                res.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "#":
            return None
        root = TreeNode(int(vals[0]))
        stack = [root]
        i = 1

        while stack:
            node = stack.pop(0)
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                stack.append(node.left)
            i += 1
            if vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                stack.append(node.right)
            i += 1

        return root