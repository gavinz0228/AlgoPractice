from collections import Counter
from heapq import heappush, heappop, heapify
class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        temp = [ (c, n) for n,c in count.items()]
        h = temp[:k]
        maxn = max(h, key=lambda x: x[0])
        heapify(h)
        for p in temp[k:]:
            maxn = p
            heappush(h, p)
            heappop(h)
        return [n[1] for n in h]