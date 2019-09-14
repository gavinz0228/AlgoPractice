class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0
        for _ in range(32):
            if x % 2 != y % 2:
                diff += 1
            x, y = x >> 1, y >> 1
        return diff
