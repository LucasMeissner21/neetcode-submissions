# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Iterative BFS Serialization

        if not root: # Delimiter for no children
            return "#"
        res = []
        stack = [root]

        # BFS Loop
        while stack:
            node = stack.pop(0)
            if not node:
                res.append("#")
            else: # Add node's value to res and add left, right nodes to stack
                res.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        return ",".join(res) # Delimit values with ','
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Iterative BFS Deserialization

        vals = data.split(",") # Split around ',' delimiter

        if vals[0] == "#": # No input
            return None
        root = TreeNode(int(vals[0]))
        stack = [root]
        i = 1

        # BFS Loop
        while stack:
            node = stack.pop(0)
            if vals[i] != "#": # Left node will always follow parent (if it exists)
                node.left = TreeNode(int(vals[i]))
                stack.append(node.left)
            i += 1
            if vals[i] != "#": # Right node will always follow left (if they exist)
                node.right = TreeNode(int(vals[i]))
                stack.append(node.right)
            i += 1

        return root