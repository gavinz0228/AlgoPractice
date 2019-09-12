class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        max_count = 1
        self.length = length
        self.s = s
        for i in range(1, length):
            count = self.count(i, - 1)
            max_count += count 
            count = self.count(i, 0)
            max_count += count
        return max_count
    
    def count(self, i, offset):
        count = 1 
        if offset == -1:
            if self.s[i] != self.s[i-1]:
                return 0
        while i + count < self.length and i - count +offset >= 0:
            if self.s[i + count] == self.s[i - count +offset]:
                count += 1
            else:
                break
        return count 
