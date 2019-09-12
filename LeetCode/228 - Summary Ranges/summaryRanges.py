class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sol = []
        last = nums[0]
        minn = last
        maxn = last
        for i in range(1, len(nums)):
            if nums[i] - 1 == last:
                maxn = nums[i]
            else:
                if minn == maxn:
                    sol.append(str(minn))
                else:
                    sol.append(str(minn)+"->"+str(maxn))
                minn = nums[i]
                maxn = nums[i]
            last = nums[i]
        if minn == maxn:
            sol.append(str(minn))
        else:
            sol.append(str(minn)+"->"+str(maxn))
        
        return sol