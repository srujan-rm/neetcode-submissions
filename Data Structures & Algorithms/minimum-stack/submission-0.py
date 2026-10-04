from collections import deque
class MinStack:
    def __init__(self):
        self.basic = deque()
        self.possible = deque()
    def push(self, val: int) -> None:
        self.basic.append(val) 
        if (len(self.possible) != 0 and self.possible[-1] < val):
            return 
        self.possible.append(val)
    def pop(self) -> None:
        if (self.basic[-1] == self.possible[-1]):
            self.possible.pop()
        self.basic.pop()

    def top(self) -> int:
        return(self.basic[-1])

    def getMin(self) -> int:
        return(self.possible[-1])
