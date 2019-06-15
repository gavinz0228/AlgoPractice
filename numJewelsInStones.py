import itertools 
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = set([ c for c in J])
        return sum([1 for c in S if c in s])
