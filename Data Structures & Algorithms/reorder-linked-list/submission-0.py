# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque 
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        stack = deque()
        iterator, count = head, 0
        while (iterator):
            count += 1
            stack.append(iterator)
            iterator = iterator.next
        iterator = head 
        for i in range(0, math.floor(count / 2)):
            next_iterator = iterator.next
            last_one = stack.pop()
            iterator.next = last_one
            iterator.next.next = next_iterator 
            iterator = next_iterator
        iterator.next = None