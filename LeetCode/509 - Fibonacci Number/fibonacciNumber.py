class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        b, c = 0, 1
        for _ in range(2, N + 1):
            b, c = c, b + c
        return c
