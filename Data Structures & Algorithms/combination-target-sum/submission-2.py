class Solution:
    def generate(self, soln, trace, index, take, target, nums):
        if (target < 0):
            return
        if (index >= len(nums)):
            return
        if (take):
            trace.append(nums[index])
            if (target == 0):
                soln.append(trace.copy())
                trace.pop()
                return
            self.generate(soln, trace, index, True, target - nums[index], nums)
            self.generate(soln, trace, index, False, target, nums)
            trace.pop()
            return
        else:
            new_index = index + 1 
            to_sub = nums[new_index] if new_index < len(nums) else 0
            self.generate(soln, trace, new_index, True, target - to_sub, nums)
            self.generate(soln, trace, new_index, False, target, nums)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        soln = []
        trace = []
        self.generate(soln, trace, 0, True, target - nums[0], nums) 
        self.generate(soln, trace, 0, False, target, nums)
        return soln