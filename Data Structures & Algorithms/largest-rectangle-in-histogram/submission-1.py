from collections import deque 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # For each index, calculate max rectangle 
        n = len(heights) 
        resultant = float("-inf") 
        rightBoundary = [0] * n 
        leftBoundary = [0] * n
        stack = deque()   
        for i in range(0, n):
            while (len(stack) > 0 and heights[stack[-1]] > heights[i]):
                obtained = stack[-1]
                rightBoundary[obtained] = i - obtained
                stack.pop() 
            stack.append(i)
        while (len(stack) > 0):
            obtained = stack.pop()
            rightBoundary[obtained] = n - obtained 
        for i in range(n - 1, -1, -1):
            while (len(stack) > 0 and heights[stack[-1]] > heights[i]):
                obtained = stack[-1]
                leftBoundary[obtained] = obtained - i 
                stack.pop()
            stack.append(i)
        while (len(stack) > 0):
            obtained = stack.pop()
            leftBoundary[obtained] = obtained + 1
        for i in range(0, n):
            resultant = max(resultant, (rightBoundary[i] + leftBoundary[i] - 1) * heights[i])
        return resultant
