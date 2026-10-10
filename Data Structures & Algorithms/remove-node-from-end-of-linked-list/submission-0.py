# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lp, rp = head, head
        pre, post = None, head.next
        for i in range(0, n - 1):
            rp = rp.next 
        while (rp.next):
            rp = rp.next 
            pre = lp
            lp = lp.next
            post = lp.next if lp.next else None
        if pre:
            pre.next = post 
        else:
            head = post
        return head

