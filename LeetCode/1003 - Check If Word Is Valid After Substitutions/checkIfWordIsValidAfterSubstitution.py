class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        last = S
        new = last.replace("abc", "")
        while new != last:
            last = new
            new = last.replace("abc", "")
        return len(new) == 0
