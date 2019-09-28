class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        length = len(bits)
        last = 0
        while i < length:
            if bits[i] == 1:
                last = 2
            else:
                last = 1
            i += last
        if i - last == length -1:
            return True
        else:
            return False
