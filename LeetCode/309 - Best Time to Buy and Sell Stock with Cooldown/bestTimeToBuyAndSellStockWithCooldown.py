from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.prices = prices
        self.length = len(prices)
        if not prices:
            return 0
        self.profit = 0
        self.aux(0, [], 0)
        return self.profit

    def aux(self, i, bs, cur):
        if i == self.length:
            if cur > self.profit:
                self.profit = cur
            return
        if len(bs) == 0:
            self.aux(i+1, bs, cur)
            self.aux(i+1,bs+[i], cur)
        elif len(bs) == 1:
            profit = self.prices[i] - self.prices[bs[0]]
            if profit > 0:
                self.aux(i+1, bs+[i], cur + profit)
            self.aux(i+1, bs, cur)
        else:
            self.aux(i+1,[], cur)
print(Solution().maxProfit([1,2,3,0,2]))