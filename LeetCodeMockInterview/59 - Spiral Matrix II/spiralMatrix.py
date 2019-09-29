class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [ [0]*n for i in range(n)]
        i = 1
        ubound, lbound = 0, 0
        bbound, rbound = n - 1, n - 1
        dcount = 0
        target = n ** 2
        r, c = 0, 0
        while i <= target:
            d = dcount % 4 
            res[r][c] = i
            if d == 0:
                if c == rbound:
                    ubound += 1
                    r += 1
                    dcount += 1
                else:
                    c += 1
                    
            if d == 1:
                if r == bbound:
                    rbound -= 1
                    c -= 1
                    dcount += 1
                else:
                    r += 1
            if d == 2:
                if c == lbound:
                    bbound -= 1
                    r -= 1
                    dcount += 1
                else:
                    c -= 1   
            if d == 3:
                if r == ubound:
                    lbound += 1
                    c += 1
                    dcount +=1
                else:
                    r -= 1
            i += 1
        return res