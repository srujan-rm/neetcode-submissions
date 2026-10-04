from collections import deque 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque() 
        for i in s:
            if (i in {"(", "{", "["}):
                stack.append(i)
            elif (i == ']'):
                if (len(stack) != 0 and stack[-1] == '['):
                    stack.pop() 
                else:
                    return False 
            elif (i == ')'):
                if (len(stack) != 0 and stack[-1] == '('):
                    stack.pop()
                else:
                    return False
            else:
                if (len(stack) != 0 and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
        return(len(stack) == 0) 
