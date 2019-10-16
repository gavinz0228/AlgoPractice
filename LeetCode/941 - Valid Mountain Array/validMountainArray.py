class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        up = None
        down = None
        length = len(A)
        for i in range(1, length):
            if A[i] == A[i - 1]:
                return False
            elif A[i] > A[i-1]:
                if up is None:
                    up = True
                if down:
                    return False
            elif A[i] < A[i - 1]:
                if up is None:
                    return False
                if down is None:
                    down = True
        if not up or not down:
            return False
        return True
