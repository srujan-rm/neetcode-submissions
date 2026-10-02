class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums: 
            if (num not in hash):
                hash[num] = 1
            else:
                hash[num] += 1
                if (hash[num] == 2):
                    return True
        return False
        