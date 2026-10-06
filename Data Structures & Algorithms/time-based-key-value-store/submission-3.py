class TimeMap:
    def __init__(self):
        self.dictionary = dict() 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = [] 
        self.dictionary[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        # find the next smallest element 
        if (key not in self.dictionary):
            return ""
        lp, rp = 0, len(self.dictionary[key]) - 1
        soln = ""
        while (lp <= rp):
            mid = lp + ((rp - lp) // 2)
            if (self.dictionary[key][mid][0] < timestamp):
                soln = self.dictionary[key][mid][1]
                lp = mid + 1 
            elif (self.dictionary[key][mid][0] > timestamp):
                rp = mid - 1 
            else:
                return self.dictionary[key][mid][1]
        return soln
