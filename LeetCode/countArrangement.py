class Solution:
    def countArrangement(self, N: int) -> int:
        nums = [ i for i in range(N, 0, -1)]
        self.sol = 0
        self.aux(nums, [])
        return self.sol
    def aux(self, nums, cur):
        cl = len(cur)
        nl = len(nums)
        for i in range(nl):
            n = nums[i]
            if n % (cl+1) == 0 or (cl+1) % n == 0 :
                if nl == 1:
                    self.sol += 1
                else:
                    nums.pop(i)
                    cur.append(n)
                    self.aux(nums, cur)
                    cur.pop()
                    nums.insert(i, n)
