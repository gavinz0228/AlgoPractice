class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        if left < 10:
            res = list(range(left, 10))
            left = 11
        for i in range(left, right + 1):
            n = i
            while n != 0:
                remainder = n % 10
                if remainder == 0:
                    break
                if i % remainder != 0:
                    break
                n = int(n/10)
            if n == 0:
                res.append(i)
        return res