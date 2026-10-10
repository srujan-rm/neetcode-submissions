class ListNode:
    def __init__(self, val, next):
        self.val = val 
        self.next = next 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # not only detect if there are duplicates
        # are there duplicates? we could use 
        tortoise, hare = 0, 0
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise] 
            if (hare == tortoise):
                break
        tortoise = 0
        while (tortoise != hare):
            tortoise = nums[tortoise]
            hare = nums[hare] 
        return hare
