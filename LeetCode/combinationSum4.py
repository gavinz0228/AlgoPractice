class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0]
        ns = set(nums)
        for i in range(1, target + 1):
            cur = 0
            if i in ns:
                cur = 1
            for n in nums:
                if i - n > 0:
                    cur += dp[i-n]
            dp.append(cur)
        return dp[-1]
