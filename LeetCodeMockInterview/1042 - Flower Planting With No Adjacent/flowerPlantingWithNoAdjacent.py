from collections import defaultdict
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [None] * N
        garden = defaultdict(list)
        for f, t in paths:
            garden[f-1].append(t-1)
            garden[t-1].append(f-1)
        for i in range(N):
            neighbors = set([])
            for aj in garden[i]:
                neighbors.add(res[aj])
            for n in range(1, 5):
                if n not in neighbors:
                    res[i] = n
                    break

        return res