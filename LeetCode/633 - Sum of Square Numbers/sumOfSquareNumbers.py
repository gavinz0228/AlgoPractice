class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lookup = set()
        ceiling = int(c ** 0.5) + 1
        for i in range(ceiling):
            lookup.add(i**2)
        for s in lookup:
            if c - s in lookup:
                return True
        return False
