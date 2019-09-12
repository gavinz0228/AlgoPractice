class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.nums = [ i for i in range(10)]
        self.num_flags = [ False for i in range(10)]
        self.num_final_flags = [ False for i in range(10)]
        self.sol = []
        self.aux([], 0, 1)
        return self.sol
    def aux(self, cur, curSum, level):
        curlen = len(cur)
        if self.k == curlen:
            if curSum == self.n:
                self.sol.append(cur)
                return True
            else:
                return False
            
        for i in range(level,len(self.num_flags)):
            if not self.num_flags[i] and not self.num_final_flags[i]:
                n = self.nums[i]
                self.num_flags[i] = True
                found = self.aux(cur + [n], curSum + n,  i + 1)
                self.num_flags[i] = False
                if found:
                    self.num_final_flags[i] = False
                
