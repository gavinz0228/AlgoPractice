class Solution:
    def check(self, mid):
        lower = mid*mid
        if lower == self.target:
            return "e"
        upper = (mid+1)*(mid + 1)
        if self.target >= upper :
            return "ts"
        elif self.target < lower:
            return "tb"
        else:
            return "e"
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        self.target = x
        hi = x
        lo = 1
        while lo < hi:
            mid = int((hi+lo) / 2)
            res = self.check(mid)
            if res == "e":
                return mid
            elif res == "tb":
                hi = mid
            else:
                lo = mid
            

            
