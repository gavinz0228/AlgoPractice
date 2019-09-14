from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        return count.get("U", 0) == count.get("D", 0) and count.get("L", 0) == count.get("R", 0)
