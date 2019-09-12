from heapq import heapify,heappush, heappop, nlargest
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -1 * s for s in stones]
        heapify(stones)
        while len(stones) >= 2:
            first = heappop(stones)
            second = heappop(stones)
            diff = abs(first - second)
            if diff > 0:
                heappush(stones, -1 * diff)
            
        l = len(stones)
        if l == 1:
            return -1 * heappop(stones)
        else:
            return 0
