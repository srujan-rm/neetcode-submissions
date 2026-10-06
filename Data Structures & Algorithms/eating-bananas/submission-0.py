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
        # what is the K such that you can eat all of them without exceeding time limit?
        # No matter the order of the pile, you'll finish all the bananas in the same time! 
        # At min k = 1, you finish at T = 10 hours 
        # 1 (NO), 2 (YES), 3 (YES), ...., MAX (YES)
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