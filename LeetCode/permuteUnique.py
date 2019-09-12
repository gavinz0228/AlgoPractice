class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        self.nums = nums
        self.length = len(nums)
        self.flags = [True for i in range(self.length)]
        self.sol = []
        self.aux([])
        return self.sol
    def aux(self, cur):
        if self.length == len(cur):
            self.sol.append(cur)
        else:
            last_num = None
            for i,f in enumerate(self.flags):
                if f and self.nums[i] != last_num:
                    self.flags[i] = False
                    self.aux(cur + [self.nums[i]])
                    self.flags[i] = True
                    last_num = self.nums[i]
        
