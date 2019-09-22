class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        self.length = len(s)
        self.s = s
        self.sol = 0
        for i in range(self.length - 1):
            if s[i] != s[i + 1]:
                self.sol += 1
                self.extend(i, i+1)
        return self.sol

    def extend(self, left, right):
        left -= 1
        right += 1
        while left > -1 and right < self.length:
            if self.s[left] == self.s[left + 1] and self.s[right] == self.s[right - 1]:
                self.sol += 1
            else:
                return
            left -= 1
            right += 1
