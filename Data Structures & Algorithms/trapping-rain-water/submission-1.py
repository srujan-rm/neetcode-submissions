class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lp, rp = 1, n - 2
        greatest_right = height[n - 1] 
        greatest_left = height[0]
        total = 0
        while (lp < rp):
            if (greatest_left < greatest_right):
                if (greatest_left - height[lp] > 0):
                    total += greatest_left - height[lp]
                greatest_left = max(greatest_left, height[lp])
                lp += 1
            else:
                if (greatest_right - height[rp] > 0):
                    total += greatest_right - height[rp] 
                greatest_right = max(greatest_right, height[rp])
                rp -= 1
        if (lp == rp):
            result = min(greatest_left, greatest_right) - height[lp]
            if (result > 0):
                total += result

        return total 
