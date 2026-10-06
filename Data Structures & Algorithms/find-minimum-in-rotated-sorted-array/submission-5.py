class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lp, rp = 0, n - 1
        soln = 1000
        while (lp <= rp):
            mid = lp + ((rp - lp) // 2)
            if (nums[rp] < nums[mid]):
                lp = mid + 1 
            else:
                soln = min(soln, nums[mid])
                rp = mid - 1
        return soln