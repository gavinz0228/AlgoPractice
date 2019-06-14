class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        res = [[]]
        for x in nums:
            l = len(res)
            for i in range(l):
                res.append(res[i] + [x])
                result.add(tuple(sorted(res[i] + [x])))
        result.add(tuple())
        return result
