from functools import lru_cache
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        lookup = defaultdict(int)
        if nums[0] != 0:
            lookup[nums[0]] = 1
            lookup[-nums[0]] = 1
        else:
             lookup[0] = 2
        for i in range(1, len(nums)):
            newlookup = defaultdict(int)
            for n,c in lookup.items():
                newlookup[n + nums[i]] += c 
                newlookup[n - nums[i]] += c
            lookup = newlookup
        return lookup[S]
                