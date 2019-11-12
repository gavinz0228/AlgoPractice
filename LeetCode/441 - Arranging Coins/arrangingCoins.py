class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        level = 0
        while True:
            if n < level:
                return level - 1
            n -= level
            level += 1

