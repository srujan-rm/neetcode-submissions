class Solution:
    def generate(self, soln, trace, nums, index, take):
        n = len(nums)
        if take:
            trace.append(nums[index])
            if (index == n - 1):
                soln.append(trace.copy())
                trace.pop()
                return
            self.generate(soln, trace, nums, index + 1, True)
            self.generate(soln, trace, nums, index + 1, False)
            trace.pop()
            return
        else:
            if (index == n - 1):
                soln.append(trace.copy())
                return
            new_index = index + 1 
            if (nums[new_index] == nums[index]):
                self.generate(soln, trace, nums, new_index, False)
                return
            self.generate(soln, trace, nums, new_index, True)
            self.generate(soln, trace, nums, new_index, False)
            return
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        soln = []
        trace = []
        self.generate(soln, trace, nums, 0, True)
        self.generate(soln, trace, nums, 0, False)
        return soln