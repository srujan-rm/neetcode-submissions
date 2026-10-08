class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lp, rp, record, reference = 0, -1, dict(), dict()
        n = len(s)
        min_size = float("inf")
        minimum_string = "" 
        total_chars = len(t)
        for i in t:
            record[i] = record.get(i, 0) + 1 
            reference[i] = reference.get(i, 0) + 1 
        while (rp < n - 1):
            rp += 1
            if (s[rp] in reference):
                reference[s[rp]] -= 1
                if (reference[s[rp]] >= 0):
                    total_chars -= 1
            while (lp <= rp and total_chars == 0 and (s[lp] not in reference or reference[s[lp]] < 0)):
                if s[lp] not in reference:
                    lp += 1
                elif reference[s[lp]] < 0:
                    reference[s[lp]] += 1
                    lp += 1
            if (total_chars == 0 and rp - lp + 1 < min_size):
                min_size = rp - lp + 1 
                minimum_string = s[lp : rp + 1]     
        return minimum_string 
