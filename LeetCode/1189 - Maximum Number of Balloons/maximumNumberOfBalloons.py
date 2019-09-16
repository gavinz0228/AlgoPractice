from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min([count.get("b", 0), count.get("a", 0), int(count.get("l", 0)/2), int(int(count.get("o", 0)/2)),count.get("n", 0) ])