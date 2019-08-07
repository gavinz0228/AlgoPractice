class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        sol = [ [nums[0]] ]
        for i in range(1, len(nums)):
            new_sol = []
            for s in sol:
                for j in range(len(s) + 1):
                    new_sol.append(s[0:j] + [nums[i]] + s[j:])
            sol = new_sol
        return sol
                    
