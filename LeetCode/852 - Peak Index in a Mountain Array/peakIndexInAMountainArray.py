from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        while True:
            if A[i] > A[i + 1]:
                return i
            i += 1
