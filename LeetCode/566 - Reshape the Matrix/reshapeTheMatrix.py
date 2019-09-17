from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        height = len(nums)
        width = len(nums[0])
        if height * width != r * c:
            return nums
        res = []
        iterator = iter(self.yield_value(nums))
        for i in range(r):
            row = []
            for j in range(c):
                row.append(next(iterator))
            res.append(row)
        return res

    def yield_value(self, nums):
        for row in nums:
            for cell in row:
                yield cell
