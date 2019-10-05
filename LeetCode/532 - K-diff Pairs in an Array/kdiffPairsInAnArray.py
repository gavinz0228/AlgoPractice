from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        count = Counter(nums)
        zero_k_pair_count = 0
        set_sol = set([])
        if k == 0:
            for n, c in count.items():
                if c > 1:
                    zero_k_pair_count += 1
            return zero_k_pair_count
        else:
            for n, c in count.items():
                if n - k in count:
                    set_sol.add(tuple(sorted([n, n - k])))
                if n + k in count:
                    set_sol.add(tuple(sorted([n, n + k])))
            return len(set_sol)
