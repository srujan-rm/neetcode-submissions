# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Suppose two linked lists, we can easily iterate and merge
        # Multiple linked lists? We can't do two two two. Very inefficient
        # How to merge multiple K sorted linked lists
        head, trail = None, None
        reserve = []
        count = 0
        # Worst case: NLlog(NL)
        # Best case: NLlog(N) 
        for l in lists: 
            if (l):
                heapq.heappush(reserve, (l.val, count, l))
                count += 1
        while (len(reserve) != 0): 
            l_val, _, l = heapq.heappop(reserve)
            node = ListNode(l_val, None)
            if not trail:
                head = node
            else:
                trail.next = node 
            trail = node
            if (l.next):
                heapq.heappush(reserve, (l.next.val, count, l.next))
                count += 1
        return head

        