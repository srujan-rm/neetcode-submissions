class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [] 
        for i in s: 
            if (i.isalnum()):
                arr.append(i.lower())
        new_string = "".join(arr)
        n = len(new_string) 
        lp, rp = 0, n - 1
        while (lp < rp):
            if (new_string[lp] != new_string[rp]):
                return False
            lp += 1 
            rp -= 1 
        return True