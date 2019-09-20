class Solution:
    def binaryGap(self, N: int) -> int:
        max_gap = 0
        i = 0
        last1 = None
        while N:
            if N % 2 == 1:
                if last1 is not None:
                    if i - last1 > max_gap:
                        max_gap = i - last1
                last1 = i
            N = int(N / 2)
            i += 1
        return max_gap
