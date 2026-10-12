import heapq 
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head, trail = None, None
        reserve = []
        count = 0
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

        