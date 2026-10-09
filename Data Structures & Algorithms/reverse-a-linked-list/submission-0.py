# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head can be null or ListNode of the Linked List
        # needs to output null or ListNode of the Linked List
        if not head:
            return None 
        element = head
        trail_pointer = None
        while element:
            node = ListNode(element.val, trail_pointer)
            trail_pointer = node
            element = element.next 
        return trail_pointer 