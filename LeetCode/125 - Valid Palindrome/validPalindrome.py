class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        l, r = 0, length - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l >= r:
                return True

            elif s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
