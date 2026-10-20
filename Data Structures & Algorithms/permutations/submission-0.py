class Solution:
    def take(self, soln, trace, nums, index, left):
        
        trace.append(nums[index]) 
        old_value = nums[index]
        nums[index] = -11 
        if (left == 0):
            soln.append(trace.copy()) 
            trace.pop()
            nums[index] = old_value
            return
        n = len(nums)
        for i in range(0, n):
            if (nums[i] == -11):
                continue
            self.take(soln, trace, nums, i, left - 1)
        nums[index] = old_value
        trace.pop()
        return
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        soln = []
        trace = []
        left = len(nums)
        n = len(nums)
        for i in range(0, n):
            self.take(soln, trace, nums, i, left - 1)
        return soln 