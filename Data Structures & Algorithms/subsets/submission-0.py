class Solution:
    def generate(self, soln, trace, index, take, nums):
        if index >= len(nums) and take:
            new_copy = trace.copy()
            soln.append(new_copy)
            return
        elif index >= len(nums):
            return
        if take:
            trace.append(nums[index])
            self.generate(soln, trace, index + 1, True, nums)
            self.generate(soln, trace, index + 1, False, nums)
            trace.pop()
            return
        else:
            self.generate(soln, trace, index + 1, True, nums)
            self.generate(soln, trace, index + 1, False, nums)
            return
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # unique integers
        # return all possible subsets of nums 
        soln = []
        trace = []
        self.generate(soln, trace, 0, True, nums) # all subsets containing 0 
        self.generate(soln, trace, 0, False, nums) # all subsets that do not contain 0
        return soln