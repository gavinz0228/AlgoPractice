class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sol = set(tiles[0])
        length = len(tiles)
        for i in range(1, length): 
            to_add = []
            for x in sol:
                for j in range(length):
                    to_add.append(x[:j] + tiles[i] + x[j:])
            sol.update(to_add)
            sol.add(tiles[i])
        return len(sol)
        
