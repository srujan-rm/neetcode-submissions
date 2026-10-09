# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tortoise, hare = head, head
        while (True):
            hare = hare.next 
            if not hare:
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