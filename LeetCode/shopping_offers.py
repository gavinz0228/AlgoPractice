class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        if not needs or sum(price) == 0:
            return 0
        return self.aux(price, special, needs, 0)
    def aux(self, price, special, needs, cost):
        num = len(needs)
        found = False
        best = sum([ needs[i] * price[i] for i in range(num)]) + cost
        for s in special:
            left = [ needs[i] - s[i] for i in range(num)]
            if min(left) >= 0:
                found = True
                if sum(left) == 0:
                    return s[-1] + cost
                else:
                    _cost = self.aux(price, special, left, s[-1] + cost)
                    if _cost < best:
                        best = _cost
                    
        return best
