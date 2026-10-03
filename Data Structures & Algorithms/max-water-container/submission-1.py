class Solution:
    def vol(self, l, r, heights): 
        return(min(heights[l], heights[r]) * (r - l))
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        lp, rp = 0, n - 1
        soln = float("-inf") 
        while (lp < rp):
            obtain_vol = self.vol(lp, rp, heights)
            # We want the value between array. Two Pointer nice approach
            # If I start from sides, how do I find the best options?
            soln = max(soln, obtain_vol)
            if (heights[lp] < heights[rp]):
                lp += 1 
            elif (heights[lp] > heights[rp]):
                rp -= 1
            else:
                lp += 1
        return soln