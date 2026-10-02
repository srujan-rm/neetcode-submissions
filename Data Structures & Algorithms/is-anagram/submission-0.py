class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_trace = [0] * 26
        t_trace = [0] * 26 
        for i in s:
            s_trace[ord(i) - ord('a')] += 1 
        for i in t:
            t_trace[ord(i) - ord('a')] += 1 
        for i, j in zip(s_trace, t_trace):
            if (i != j):
                return False
        return True