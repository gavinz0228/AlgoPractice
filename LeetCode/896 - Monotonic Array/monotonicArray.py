class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        length = len(A)
        if length == 1:
            return True
        sign = None
        for i in range(1, length):
            if A[i] != A[i - 1]:
                sign = A[i] - A[i - 1]
                break
        for i in range(i + 1, length):
            if (A[i] - A[i - 1]) * sign < 0:
                return False
        return True