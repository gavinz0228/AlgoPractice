class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        def product(lst):
            a, b, c = lst
            return a*b*c
        return max(product(nums[-3:]), product(nums[:2] + nums[-1:]))