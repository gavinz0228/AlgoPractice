class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sol = []
        num_set = set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                sol.append(n)
        return sol
