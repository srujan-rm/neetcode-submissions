from collections import deque 
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to preserve history 
        stack = deque() 
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                op2 = stack.pop() 
                op1 = stack.pop()
                result = 0
                if (i == '+'):
                    result = op1 + op2 
                elif (i == '-'):
                    result = op1 - op2
                elif (i == '*'):
                    result = op1 * op2 
                else:
                    result = int(op1 / op2)
                stack.append(result)
            else:
                stack.append(int(i)) 
        return(stack.pop())