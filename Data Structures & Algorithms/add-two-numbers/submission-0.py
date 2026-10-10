# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 321, stored as 1 --> 2 --> 3 
        # add two numbers 
        # 1-->2-->3 (321)
        # 4-->5-->6 (654)
        it1, it2, carry = l1, l2, 0
        head, trail = None, None
        while it1 and it2:
            resultant = it1.val + it2.val + carry
            value = (resultant - 10) if (resultant >= 10) else resultant 
            carry = 1 if (resultant >= 10) else 0 
            node = ListNode(value)
            it1, it2 = it1.next, it2.next
            if (not head):
                head = node 
                trail = head 
            else:
                trail.next = node 
                trail = node
        while it2:
            resultant = it2.val + carry + 0
            value = (resultant - 10) if (resultant >= 10) else resultant
            carry = 1 if (resultant >= 10) else 0 
            node = ListNode(value)
            it2 = it2.next
            if (not head):
                head = node 
                trail = head 
            else:
                trail.next = node
                trail = node
        while it1:
            resultant = it1.val + carry + 0
            value = (resultant - 10) if (resultant >= 10) else resultant
            carry = 1 if (resultant >= 10) else 0 
            node = ListNode(value)
            it1 = it1.next
            if (not head):
                head = node 
                trail = head 
            else:
                trail.next = node
                trail = node
        
        if (carry):
            trail.next = ListNode(1)
            trail = trail.next
        return head
        # 3217 + 654
        # 7->1->2->3 + 4->5->6


