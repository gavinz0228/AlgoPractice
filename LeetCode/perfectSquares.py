import math
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0, 1]
        for i in range(2, n+1):
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
