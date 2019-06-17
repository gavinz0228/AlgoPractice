class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = []
        length = len(A)
        for i in range(length):
            if not s or A[i] < A[s[-1]]:
                s.append(i)
        output = 0
        for i in range(length - 1, -1, -1):

            while s and A[i] >= A[s[-1]]:
                output = max(output, i - s.pop())
        return output
