from collections import Counter
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n,c in Counter(nums).items():
            if c > 1: return n
        