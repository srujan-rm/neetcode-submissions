# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # head is None or head is ListNode 
        # return true if there is a cycle in head, or return false
        # cycle in linked list if we go back to a node that was visited
        if not head:
            return False
        tortoise = head 
        hare = head 
        while (True):
            hare = hare.next 
            if (not hare):
                return False
            if (hare == tortoise):
                return True 
            hare = hare.next 
            if (not hare):
                return False 
            if (hare == tortoise):
                return True 
            tortoise = tortoise.next 
        return False