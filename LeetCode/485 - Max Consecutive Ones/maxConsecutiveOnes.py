class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last = -1
        maxs = 0
        for i, n in enumerate(nums):
            if n == 0:
                maxs = max(maxs, i - last - 1)
                last = i
        maxs = max(maxs, len(nums) - last - 1)
        return maxs
