from collections import deque
class Solution:
    def __init__(self):
        self.global_n = None
    def generate(self, trace, soln, open_left, close_left, open_use):
        if (open_use):
            trace.append('(')
            if (open_left > 0):
                self.generate(trace, soln, open_left - 1, close_left, True)
                self.generate(trace, soln, open_left, close_left - 1, False)
            else:
                self.generate(trace, soln, open_left, close_left - 1, False)
            trace.pop()
            return
        else:
            trace.append(')')
            if (open_left == 0 and close_left == 0):
                soln.append("".join(trace))
                trace.pop()
                return
            if (open_left == close_left):
                self.generate(trace, soln, open_left - 1, close_left, True)
                trace.pop()
                return
            if (open_left > 0):
                self.generate(trace, soln, open_left - 1, close_left, True)
            self.generate(trace, soln, open_left, close_left - 1, False)
            trace.pop()
            return
            

    def generateParenthesis(self, n: int) -> List[str]:
        open_left, close_left, trace, soln = n, n, [], []
        self.global_n = n
        self.generate(trace, soln, open_left - 1, close_left, True)  
        return soln