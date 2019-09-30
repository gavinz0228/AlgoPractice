from collections import deque


class Solution:
    def convertToTitle(self, n: int) -> str:
        lookup = {i: chr(65 + i) for i in range(26)}
        q = deque([])
        if n == 0:
            return "A"
        while n != 0:
            n -= 1
            q.appendleft(lookup[n % 26])
            n = int(n / 26)
        return "".join(q)
