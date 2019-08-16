class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.getString(s)[0] 
    def getChars(self, s):
        if not s:
            return "",""
        if ord(s[0]) > 57:
            for i in range(len(s)):
                if ord(s[i]) <= 57 or s[i]== "]":
                    return s[:i] , s[i:]
            return s, ""
        else:
            return "", s
    def getString(self, s):
        result = []
        while s and s[0] != "]":
            _s, _tail = self.getChars(s) 
            __s, __tail = self.getNum(_tail) 
            result.append(_s+__s)
            s = __tail
        return "".join(result), s
    def getNum(self, s):
        if not s:
            return "",""
        if ord(s[0]) <= 57:
            lb = s.index("[")
            chars, tail = self.getString( s[lb+1:] )
            n = int(s[:lb])
            return n*chars, tail[1:]
        else:
            return "", s