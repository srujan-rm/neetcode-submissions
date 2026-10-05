from collections import deque 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        n = len(temperatures)
        resultant = [0] * n
        for i in range(0, n):
            if (len(stack) == 0):
                stack.append(i)
            else:
                while (len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]):
                    to_process = stack.pop()
                    resultant[to_process] = i - to_process
                stack.append(i)
        return resultant