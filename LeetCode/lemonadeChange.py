class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = 0
        t = 0
        tw = 0
        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                if f == 0:
                    return False
                else:
                    f -= 1
                t += 1
            else:
                
                if t > 0 and f > 0:
                    t -= 1
                    f -= 1
                elif f >= 3:
                    f -= 3
                else:
                    return False
                tw += 1
        return True
