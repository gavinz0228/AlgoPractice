class Solution:
    def tribonacci(self, n: int) -> int:
        base = [0, 1, 1]
        if n < 3:
            return base[n]
        for i in range(3, n + 1):
            base[0], base[1], base[2] = base[1], base[2], base[0] + base[1] + base[2]
        return base[2]
