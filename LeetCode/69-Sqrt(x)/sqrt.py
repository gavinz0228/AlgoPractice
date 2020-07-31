class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        else:
            hi = int(x/2) + 1
            lo = 1
            while True:
                if hi == lo or lo + 1 == hi:
                    return lo
                else:
                    mid = int((hi + lo) / 2)
                test = mid ** 2
                if test == x:
                    return mid
                elif test > x:
                    hi = mid
                else:
                    lo = mid
            
