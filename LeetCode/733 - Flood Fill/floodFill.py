class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.height = len(image)
        self.width = len(image[0])
        self.image = image
        area = set([])
        self.findArea(sr, sc, image[sr][sc], area)
        for r, c in area:
            image[r][c] = newColor
        return image

    def findArea(self, r, c, val, area):
        if r < 0 or r == self.height or c < 0 or c == self.width or (r,c,) in area or self.image[r][c] != val:
            return
        if self.image[r][c] == val:
            area.add((r,c,))
        self.findArea(r + 1, c, val, area)
        self.findArea(r - 1, c, val, area)
        self.findArea(r, c + 1, val, area)
        self.findArea(r, c - 1, val, area)
        
        