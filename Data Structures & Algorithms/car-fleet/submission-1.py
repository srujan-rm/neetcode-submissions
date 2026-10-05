from collections import deque
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        resultant = []
        n = len(position)
        for i in range(0, n):
            resultant.append((position[i], (target - position[i]) / speed[i]))
        resultant.sort(reverse = True)
        stack = deque()
        for (pos, time) in resultant:
            if (len(stack) == 0):
                stack.append(time)
            else:
                if (time > stack[-1]):
                    stack.append(time)
        return len(stack)
        


