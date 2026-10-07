class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref_table = [0] * 26 
        check_table = [0] * 26
        for i in s1:
            ref_table[ord(i) - ord('a')] += 1 
        lp, rp, n = 0, -1, len(s2)
        remaining_chars = len(s2)
        while (rp < n - 1):
            # create invalid
            # resolve invalid
            rp += 1 
            check_table[ord(s2[rp]) - ord('a')] += 1
            while (check_table[ord(s2[rp]) - ord('a')] > ref_table[ord(s2[rp]) - ord('a')]):
                check_table[ord(s2[lp]) - ord('a')] -= 1
                lp += 1
            if (rp - lp + 1 == len(s1)):
                return True
        return False


