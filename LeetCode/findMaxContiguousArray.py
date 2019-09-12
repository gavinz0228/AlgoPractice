class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cur = 0
        hs = {0:[-1]}
        for i, x in enumerate(nums):
            if x == 0:
                cur -= 1
            else:
                cur += 1
            if cur in hs:
                hs[cur].append(i)
            else:
                hs[cur] = [i]
        maxn = 0
        for _, v in hs.items():
            n = max(v) - min(v)
            if n > maxn:
                maxn = n
        return maxn
