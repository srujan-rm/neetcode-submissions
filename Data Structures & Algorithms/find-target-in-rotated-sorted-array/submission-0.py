class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lp, rp = 0, n - 1
        while (lp <= rp):
            mid = lp + ((rp - lp) // 2)
            if (nums[mid] == target): 
                return mid
            if (nums[lp] == target):
                return lp
            if (nums[rp] == target):
                return rp
            if (nums[rp] < nums[mid]):
                if (target > nums[lp] and target < nums[mid]):
                    rp = mid - 1
                else:
                    lp = mid + 1
            else:
                if (target > nums[mid] and target < nums[rp]):
                    lp = mid + 1 
                else:
                    rp = mid - 1
        return -1