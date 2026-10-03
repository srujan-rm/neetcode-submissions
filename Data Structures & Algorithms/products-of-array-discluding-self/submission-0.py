class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solution = [0] * n
        rightProduct = 1
        leftProduct = 1
        for i in range(0, n):
            solution[i] = leftProduct
            leftProduct *= nums[i] 
        for i in range(n - 1, -1, -1):
            solution[i] *= rightProduct
            rightProduct *= nums[i] 
        return solution
            
