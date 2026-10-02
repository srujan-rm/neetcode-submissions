class Solution:
    def twoSum(self: Solution, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            if ((target - nums[i]) in hash):
                return [hash[target - nums[i]], i] 
            else:
                hash[nums[i]] = i
        return []