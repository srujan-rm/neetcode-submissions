class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        lp, rp = 0, n - 1
        while (lp < rp):
            calculated = numbers[lp] + numbers[rp]
            if (calculated > target):
                rp -= 1 
            elif (calculated < target):
                lp += 1
            else:
                return [lp + 1, rp + 1]
        return []  