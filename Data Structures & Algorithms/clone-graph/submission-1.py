"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Yea
        if not node:
            return 
        nodeMap = {}

        def dfs(node: Optional['Node']):
            if node in nodeMap:
                return
            # Create node clone and map to original
            nodeMap[node] = Node(node.val)
            for neighbor in node.neighbors:
                # Recursive call to create all neighbor nodes and add to map
                dfs(neighbor)
                nodeMap[node].neighbors.append(nodeMap[neighbor]) # Add cloned neighbor
            return

        dfs(node)

        return nodeMap[node]

            