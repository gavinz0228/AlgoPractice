

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([ words[::-1] for words in s.split(" ") if words!= "" ])