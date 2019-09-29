class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        if len(str1) > len(str2):
            self.lstr, self.sstr = str1, str2
        else:
            self.lstr, self.sstr = str2, str1
        if self.tryString(self.sstr):
            return self.sstr
        len_s = len(self.sstr)
        for i in range(2, len(self.sstr) + 1):
            if len_s % i == 0:
                if self.tryString(self.sstr[:len_s / i]):
                    return self.sstr[:len_s / i]
        return ""
            
    def tryString(self, s):
        if self.lstr.replace(s,"") == "" and self.sstr.replace(s,"") == "":
            return True
        else:
            return False