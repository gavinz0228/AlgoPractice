class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.length = len(prices)
        i = 0
        sol = 0
        while i < self.length:
            valley = self.findValley(i)
            if valley is not None:
                peak = self.findPeak(valley + 1, prices[valley])
                if peak is not None:
                    sol += prices[peak] - prices[valley]
                    i = peak + 1
                else:
                    return sol
            else:
                return sol
        return sol

    def findValley(self, idx):
        for i in range(idx, self.length - 1):
            if self.prices[i + 1] > self.prices[i]:
                return i
        return None

    def findPeak(self, idx, buy_price):
        for i in range(idx, self.length):
            if self.prices[i] > buy_price and (i + 1 == self.length or self.prices[i + 1] < self.prices[i]):
                return i
        return None
