class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        self.grid = grid
        water = set()
        self.height = len(grid)
        self.width = len(grid[0])
        max_dist = 0
        max_point = None
        for r, row in enumerate(grid):
            for c, cell in enumerate(grid[r]):
                if cell == 0:
                    water.add((r, c))

        num_water = len(water)
        if num_water == 0:
            return -1
        while water:
            water_near_land = {}
            for p in water:
                lands = self.getSuroundings(p[0], p[1])
                if lands:
                    water_near_land[p] = min(lands) + 1
            for p, val in water_near_land.items():
                if val > max_dist:
                    max_dist = val
                    max_point = p
                self.grid[p[0]][p[1]] = val
                water.remove(p)
            first_round = False
            if len(water) == num_water:
                return -1
        return max_dist - 1
    
    def getSuroundings(self, r, c):
        sur = []
        up = self.getVal(r+1, c)
        down = self.getVal(r-1, c)
        right = self.getVal(r, c+1)
        left = self.getVal(r, c-1)
        if up:
            sur.append(up)
        if down:
            sur.append(down)
        if right:
            sur.append(right)
        if left:
            sur.append(left)
        return sur

    def getVal(self, r, c):
        if r > -1 and r < self.height and c > -1 and c < self.width:
            return self.grid[r][c]
