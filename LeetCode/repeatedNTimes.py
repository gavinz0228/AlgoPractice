class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for x in A:
            if not x in s:
                s.add(x)
            else:
                return x
