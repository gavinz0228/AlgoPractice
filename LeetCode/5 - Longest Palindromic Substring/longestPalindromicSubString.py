class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result  = ""
        if len(set(s))==1:
            return s
        l = len(s)
        for i in range(l):
            
            temp = self.checkPal(s, i, l, 0, 0)
            if len(temp) > len(result):
                result = temp
            if i - 1 >= 0 and s[i-1] == s[i]:
                temp = self.checkPal(s, i, l, 1, 0)
                if len(temp) > len(result):
                    result = temp
            if i + 1 < l and s[i+1] == s[i]:
                temp = self.checkPal(s, i, l, 0, 1)
                if len(temp) > len(result):
                    result = temp
                
        return result
    def checkPal(self, s, i, l, left, right ):
        while i + right + 1< l and i - left -1 >= 0:
            
            if s[i+right + 1] == s[i-left -1]:
                right += 1
                left += 1
            else:
                break
        return s[i-left :i+right +1]