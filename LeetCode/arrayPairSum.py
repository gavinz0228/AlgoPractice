class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        return sum([ nums[i * 2] for i in range(int(l/2) ) ] )
