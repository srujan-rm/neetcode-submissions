"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.lookup = dict()
    def construct(self, head):
        if (not head):
            return None
        new_node = Node(head.val) 
        self.lookup[head] = new_node
        new_node.next = self.construct(head.next)
        new_node.random = self.lookup[head.random] if head.random else None
        return new_node
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.construct(head) 