from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # left end is greater, right end is smaller
        lp, rp, mono, n, soln = 0, -1, deque(), len(nums), []
        while (rp < k - 1):
            rp += 1
            while (len(mono) != 0 and mono[-1] < nums[rp]):
                mono.pop()
            mono.append(nums[rp])
        while (rp < n - 1):
            soln.append(mono[0]) 
            # create invalid 
            rp += 1 
            while (len(mono) != 0 and mono[-1] < nums[rp]):
                mono.pop()
            mono.append(nums[rp])
            # resolve invalid 
            if (nums[lp] == mono[0]):
                mono.popleft()
            lp += 1
        soln.append(mono[0]) 
        return soln
            