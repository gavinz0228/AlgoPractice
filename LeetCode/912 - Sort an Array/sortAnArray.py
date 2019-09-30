class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        self.aux(nums, 0, length)
        return nums

    def aux(self, nums, s, e):
        if e - s < 2:
            return
        pivot = nums[s]
        left = [n for n in nums[s+1:e] if n < pivot]
        nums[s:e] = left + [nums[s]] + [n for n in nums[s+1:e] if n >= pivot]
        pivot_index = len(left) + s
        self.aux(nums, s, pivot_index)
        self.aux(nums, pivot_index+1, e)
