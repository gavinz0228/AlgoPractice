class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.i = 0
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if not self.stack:
            self.stack.append( (price,0) )
            self.i += 1
            return 1
        if price < self.stack[-1][0]:
            self.stack.append( (price,self.i) )
            self.i += 1
            return 1
        else:
            while self.stack and self.stack[-1][0] <= price:
                self.stack.pop()
            if self.stack:
                distance = self.i - self.stack[-1][1] 
                self.stack.append( (price,self.i) )
                self.i += 1
                return  distance
            else:
                self.stack.append( (price,self.i) )
                self.i += 1
                return self.i 
                



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)