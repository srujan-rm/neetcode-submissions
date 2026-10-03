class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        maxcount = 0 
        for i in nums: 
            if (i - 1 in lookup):
                continue 
            count = 0
            duplicate = i
            while (duplicate in lookup):
                count += 1
                duplicate += 1 
            maxcount = max(maxcount, count)
        return maxcount 