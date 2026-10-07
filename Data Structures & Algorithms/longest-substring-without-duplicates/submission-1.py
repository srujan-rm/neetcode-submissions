class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Given string 's', find the length of the longest substring without duplicate characters
        # Can I apply sliding window? 
        # Assume this is the required length of the longest substring 
        # Sliding window does accommodate the substring.
        # Also, it is monotonic. 
        # Remember, sliding window is always monotonic!! 
        # Perfect use 
        lp, rp, n = 0, -1, len(s)
        lookup = set()
        max_length = 0
        while (rp < n - 1):
            rp += 1
            while (s[rp] in lookup):
                lookup.remove(s[lp])
                lp += 1 
            lookup.add(s[rp])
            max_length = max(max_length, rp - lp + 1)
            # resolve invalid state
        return max_length
