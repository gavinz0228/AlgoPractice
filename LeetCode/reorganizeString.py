from collections import Counter
from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        counter = Counter(S)
        tups = [ (-1 * v, k) for k,v in counter.items()]
        heapify(tups)
        result = [ None for i in range(length)]
        idx = [ i for i in range(length) if i % 2 == 0 ]
        idx = idx + [i for i in range(length) if i % 2 == 1]
        #print(idx)
        completed = 0
        while tups:
            cur = heappop(tups)
            count = cur[0] * -1
            c = cur[1]
            for i in range(completed, count + completed ):
                tar_idx = idx[i]
                if tar_idx > 0 and result[tar_idx - 1] == c:
                    return ""
                if tar_idx < length - 1 and result[tar_idx + 1] ==c:
                    return ""
                result[tar_idx] = c
            completed = i + 1
        return "".join(result)
