class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        sol = []
        for i in range(n):
            sol.append(nums[i])
            sol.append(nums[n+i])
        return sol
