from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = defaultdict(list)
        for i, n in enumerate(nums):
            if n in lookup:
                if i - lookup[n][-1] <= k:
                    return True
            lookup[n].append(i)
        return False
