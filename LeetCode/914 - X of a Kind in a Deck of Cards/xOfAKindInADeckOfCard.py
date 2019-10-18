 from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        count = Counter(deck)
        nums = list(count.values())
        last = nums[0]
        for i in range(1, len(nums)):
            last = gcd(last, nums[i])
        if last > 1:
            return True
        else:
            return False
