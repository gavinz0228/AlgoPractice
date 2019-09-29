class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        minutes = 0
        fresh_count = 0
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.rotten = []
        for r in range(self.height):
            for c in range(self.width):
                if self.grid[r][c] == 2:
                    self.rotten.append((r, c,))
                elif self.grid[r][c] == 1:
                    fresh_count += 1
        
        if not self.rotten and not fresh_count:
            return 0
        elif not self.rotten:
            return -1
        
        while True:
            ready = set([])
            for r, c in self.rotten:
                ready.update(self.findFresh(r, c))
            if len(ready) == 0:
                break
            for r, c in ready:
                self.grid[r][c] = 2
            self.rotten.extend(ready)
            fresh_count -= len(ready)
            minutes += 1
        if fresh_count > 0:
            return -1
        return minutes
        
    def findFresh(self, r, c):
        fresh = []
        if self.isFresh(r + 1, c):
            fresh.append((r + 1, c,))
        if self.isFresh(r - 1, c):
            fresh.append((r - 1, c,))
        if self.isFresh(r, c + 1):
            fresh.append((r, c + 1,))
        if self.isFresh(r, c - 1):
            fresh.append((r, c - 1,))
        return fresh
    def isFresh(self, r, c):
        if r > -1 and r < self.height and c > -1 and c < self.width:
            return self.grid[r][c] == 1
        else:
            return False