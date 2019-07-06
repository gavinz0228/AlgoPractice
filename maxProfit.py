from collections import deque
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        dp = deque([prices[-1]])
        length = len(prices)
        for i in range(length -2, -1, -1):
            if prices[i] > dp[0]:
                dp.appendleft(prices[i] )
            else:
                dp.appendleft(dp[0])
        for i, n in enumerate(dp):
            if n - prices[i] > profit:
                profit = n - prices[i]
            
        return profit
