# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultant = None 
        if (not list1) and (not list2):
            return resultant 
        it1, it2, head = list1, list2, resultant
        while (it1 and it2):
            node = None
            if (it1.val < it2.val):
                node = ListNode(it1.val)
                it1 = it1.next
            else:
                node = ListNode(it2.val)
                it2 = it2.next
            if (not resultant):
                resultant = node 
                head = node 
            else:
                resultant.next = node 
                resultant = node 
        
        while (it1):
            node = ListNode(it1.val, None)
            it1 = it1.next
            if (not resultant):
                resultant = node 
                head = node 
            else:
                resultant.next = node
                resultant = node
 
        while (it2):
            node = ListNode(it2.val, None)
            it2 = it2.next
            if (not resultant):
                resultant = node 
                head = node 
            else:
                resultant.next = node 
                resultant = node

        return head