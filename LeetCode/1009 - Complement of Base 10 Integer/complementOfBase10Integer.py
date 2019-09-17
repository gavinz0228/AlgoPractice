class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        binary = []
        while N != 0:
            binary.append((N % 2) ^ 1)
            N = int(N / 2)
        res = 0
        for i, b in enumerate(binary):
            res += b * 2 ** i
        return res
