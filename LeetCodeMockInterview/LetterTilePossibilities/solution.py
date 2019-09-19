from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        s = set([])
        length = len(tiles)
        for i in range(1, length + 1):
            s.update(["".join(x) for x in permutations(tiles, i)])
        return len(s)
