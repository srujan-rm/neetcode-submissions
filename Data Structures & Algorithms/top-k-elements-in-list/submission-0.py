import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent elements within the array
        freq = dict() 
        minHeap = []
        solution = []
        for i in nums:
            if (i not in freq):
                freq[i] = 1 
            else:
                freq[i] += 1 
        for u, v in freq.items():
            heapq.heappush(minHeap, (v, u))
            if (len(minHeap) > k):
                heapq.heappop(minHeap)
        while (len(minHeap) > 0):
            solution.append(heapq.heappop(minHeap)[1])
        return solution
