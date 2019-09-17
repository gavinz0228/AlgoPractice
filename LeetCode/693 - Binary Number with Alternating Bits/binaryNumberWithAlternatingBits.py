

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        cur = n % 2
        n = int(n / 2)
        while n != 0:
            if n % 2 != cur ^ 1:
                return False
            cur = n % 2
            n = int(n / 2)
        return True
