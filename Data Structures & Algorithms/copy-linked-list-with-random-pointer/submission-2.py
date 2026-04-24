"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        hashMap = {}
        start = head

        prev = None
        while head: # First pass: storing deep copies in hashmap and linking them
            copy_node = Node(head.val)
            hashMap[head] = copy_node
            if prev:
                hashMap[prev].next = copy_node
            prev = head
            head = head.next
        
        head = start
        while head: # Second pass: updating random pointers in deep copy
            if head.random:
                hashMap[head].random = hashMap[head.random]
            head = head.next

        return hashMap[start]
