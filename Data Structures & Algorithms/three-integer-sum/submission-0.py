class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        n = len(nums)
        nums.sort()
        distinct_a = float("-inf") 
        for i in range(n):
            if (distinct_a != nums[i]):
                distinct_a = nums[i]
                target = 0 - nums[i]
                lp, rp = i + 1, n - 1
                while (lp < rp):
                    new_target = nums[lp] + nums[rp]
                    if (new_target < target):
                        old_recorded = nums[lp]
                        while (lp < rp and nums[lp] == old_recorded):
                            lp += 1 
                    elif (new_target > target):
                        old_recorded = nums[rp]
                        while (lp < rp and nums[rp] == old_recorded):
                            rp -= 1
                    else:
                        solution.append([nums[i], nums[lp], nums[rp]])
                        old_recorded_lp = nums[lp]
                        old_recorded_rp = nums[rp] 
                        while (lp < rp and nums[lp] == old_recorded_lp):
                            lp += 1
                        while (lp < rp and nums[rp] == old_recorded_rp):
                            rp -= 1
            else:
                continue
        return solution
                    