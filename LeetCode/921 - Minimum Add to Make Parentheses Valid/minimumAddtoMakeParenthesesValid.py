class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        num = 0
        stack = 0
        for s in S:
            if s == '(':
                stack += 1
            else:
                if stack > 0:
                    stack -= 1
                else:
                    num += 1
        return num + stack