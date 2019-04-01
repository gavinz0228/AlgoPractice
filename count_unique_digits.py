import operator
from functools import reduce
class Solution:
    def countNumbersWithUniqueDigits(self, n: 'int') -> 'int':

        digits = [9,9,8,7,6,5,4,3,2,1]
        if n ==0 :
            return 1
        s = 1
        for i in range(1, n + 1):
            uni = reduce(operator.mul, digits[:i], 1) 
            s += uni
        return s
