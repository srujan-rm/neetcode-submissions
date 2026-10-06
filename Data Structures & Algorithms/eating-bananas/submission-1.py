import math
class Solution:
    def canEat(self, h, piles, k):
        total_hours = 0
        for i in piles:
            total_hours += math.ceil(i / k)
            if (total_hours > h):
                return False 
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp, rp = 1, max(piles)
        soln = rp
        while (lp <= rp):
            mid = lp + ((rp - lp) // 2)
            if (self.canEat(h, piles, mid) == True):
                soln = mid
                rp = mid - 1
            else:
                lp = mid + 1
        return soln