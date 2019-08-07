class Solution:
    def check(self, mid):
        lower = mid*mid
        if lower == self.target:
            return 0
        upper = (mid+1)*(mid + 1)
        if self.target >= upper :
            return -1
        elif self.target < lower:
            return 1
        else:
            return 0
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        self.target = x
        hi = x
        lo = 1
        while lo < hi:
            mid = int((hi+lo) / 2)
            res = self.check(mid)
            if res == 0:
                return mid
            elif res == 1:
                hi = mid
            else:
                lo = mid
            
            
