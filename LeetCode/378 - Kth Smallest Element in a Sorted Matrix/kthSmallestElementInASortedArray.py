from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        length = len(matrix)
        idx = [0] * length
        n = 0
        for i in range(length):
            for j in range(length):
                cur = {matrix[i][idx[i]]: i for i in range(length) if idx[i]< length}
                min_val = min(cur.keys())
                row = cur[min_val]
                idx[row] += 1
                n += 1
                if n == k:
                    return min_val
