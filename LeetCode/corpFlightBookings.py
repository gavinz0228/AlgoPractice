from collections import defaultdict
class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        helper = defaultdict(int)
        for i,j,k in bookings:
            helper[i]+=k
            if j+1<=n: helper[j+1]-=k

        res=[0]*(n+1)
        for i in range(1,n+1):
            inc = helper[i] if i in helper else 0
            res[i]=res[i-1]+inc
        return res[1:]
