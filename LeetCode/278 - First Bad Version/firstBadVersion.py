# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        hi = n + 1
        low = 1
        while low <= hi:
            mid = int((hi + low) / 2)
            if not isBadVersion(mid):
                low = mid + 1
            else:
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                else:
                    hi = mid - 1
