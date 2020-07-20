class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        count = {}
        visited = 0
        for n in sorted_nums:
            if n not in count:
                count[n] = visited
            visited += 1
        sol = []
        for n in nums:
            sol.append(count[n])
        return sol
