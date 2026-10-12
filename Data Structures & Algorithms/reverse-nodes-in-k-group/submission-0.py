# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lp, rp = head, head
        prev = None
        trail = None
        soln = None
        while (rp):
            for i in range(0, k):
                if (rp):
                    prev = rp
                    rp = rp.next
                else:
                    trail.next = lp
                    return soln
            prev.next = None 
            _prev = None
            after = lp.next
            _tail = lp 
            _head = prev
            while (lp): 
                lp.next = _prev 
                _prev = lp
                lp = after 
                if (after):
                    after = after.next
            lp = rp
            if (not soln):
                soln = _head
            if (not trail):
                trail = _tail 
            else:
                trail.next = _head
                trail = _tail 

        return soln


            