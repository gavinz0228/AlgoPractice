class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(0, n+1)]
        sol = []
        for  i in range(n):
            num_groups = math.factorial(n-1)
            ith_group = math.ceil(k / num_groups)
            remainder = k % num_groups
            sol.append(nums[ith_group])
            nums.pop(ith_group)
            if remainder == 1:
                return "".join(sol) + "".join(nums[1:])
            elif remainder == 0:
                return "".join(sol) + "".join(nums[1:][::-1])
            k = remainder 
            n -= 1
            
        return "".join(sol)
