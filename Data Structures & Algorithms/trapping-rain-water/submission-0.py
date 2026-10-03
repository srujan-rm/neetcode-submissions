class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right, max_left_soln, max_right_soln = [0] * n, [0] * n, float("-inf"), float("-inf")
        n = len(height)
        for i in range(0, n):
            max_left[i] = max_left_soln 
            max_left_soln = max(max_left_soln, height[i])
            max_right[n - i - 1] = max_right_soln
            max_right_soln = max(max_right_soln, height[n - i - 1])
        total = 0
        for i in range(1, n - 1):
            level = min(max_left[i], max_right[i])
            if (level >= height[i]):
                total += level - height[i]
        return total

