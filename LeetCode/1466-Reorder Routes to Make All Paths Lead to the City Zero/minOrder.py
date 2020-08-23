from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        num_change = 0
        nei = defaultdict(list)
        paths = set()
        for p in connections:
            nei[p[0]].append(p[1])
            nei[p[1]].append(p[0])
            paths.add((p[0],p[1],))
        def find_nei(i):
            for n in nei[i]:
                nei[n].remove(i)
                if (n, i) not in paths:
                    nonlocal num_change
                    num_change += 1
                find_nei(n)
        find_nei(0)
        return num_change
