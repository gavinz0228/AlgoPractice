class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {c: chr(97 + i) for i, c in enumerate(order)}
        def map_chars(w):
            return "".join(map(lambda x: lookup[x], w))

        last = map_chars(words[0])
        for i in range(1, len(words)):
            cur = map_chars(words[i])
            if cur < last:
                return False
            last = cur
        return True
