import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        solution = []
        n = len(nums) 
        freqMap = dict()
        for i in nums:
            if (i not in freqMap):
                freqMap[i] = 1 
            else:
                freqMap[i] += 1
        freqToCount = [[] for i in range(n + 1)]
        for u, v in freqMap.items():
            freqToCount[v].append(u)
        count, start = 0, n
        while (count < k):
            if (len(freqToCount[start]) > 0):
                solution.append(freqToCount[start].pop())
                count += 1
            else:
                start -= 1
        return solution 
