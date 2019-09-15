class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.sol = []
        self.orig = n
        self.digits = list(str(n))
        self.digits.sort()
        self.length = len(self.digits)
        self.used = [False] * self.length
        self.max = 2**31
        res = self.back_track(0, 0)
        if res:
            return self.sol
        else:
            return -1
    def back_track(self, cur_idx, curr):
        digit_left = (self.length - cur_idx - 1)
        target = int(self.orig / 10 ** digit_left)
        for i, d in enumerate(self.digits): 
            if not self.used[i]:
                temp = curr * 10 + int(self.digits[i])
                if temp * 10 ** digit_left > self.max:
                    return False
                if cur_idx == self.length - 1:
                    if temp > target and temp < self.max:
                        self.sol = temp
                        return True
                    else:
                        return False
                if temp >= target:
                    self.used[i] = True
                    res = self.back_track(cur_idx + 1, temp)
                    self.used[i] = False
                    if res:
                        return res
        return False
