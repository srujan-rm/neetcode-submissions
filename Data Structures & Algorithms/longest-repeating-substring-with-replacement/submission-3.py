class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = [0] * 26
        lp, rp = 0, -1 
        maxString = 0
        n = len(s)
        while (rp < n - 1):
            rp += 1
            freq_map[ord(s[rp]) - ord('A')] += 1
            while ((rp - lp + 1) - max(freq_map) > k):
                freq_map[ord(s[lp]) - ord('A')] -= 1 
                lp += 1
            maxString = max(maxString, rp - lp + 1)
        return maxString