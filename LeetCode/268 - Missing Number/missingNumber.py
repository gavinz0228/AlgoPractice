class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return int((1+length) * length / 2 - sum(nums))
