from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        length = len(S)
        res = length * [None]
        last_idx = None
        for i, c in enumerate(S):
            if c == C:
                last_idx = i
            if last_idx is not None:
                res[i] = i - last_idx

        last_idx = None
        for i in range(length - 1, -1, -1):
            if S[i] == C:
                last_idx = i
            if last_idx is not None:
                if not res[i] or last_idx - i < res[i]:
                    res[i] = last_idx - i
        return res
