from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        lookup = {chr(97 + i): widths[i] for i in range(len(widths))}
        if not S:
            return [0, 0]
        cur = 0
        count = 1
        for c in S:
            if lookup[c] + cur > 100:
                cur = lookup[c]
                count += 1
            else:
                cur += lookup[c]
        return [count, cur]
