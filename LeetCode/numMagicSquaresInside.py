class Solution(object):
    def __init__(self):
        self.all_nums = set([1,2,3,4,5,6,7,8,9])
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        width = len(grid[0])
        height = len(grid)
        if width < 3 or height < 3:
            return 0
        num = 0
        for i in range(height - 2):
            for j in range(width - 2):
                if self.checkSquare(grid, i, j):
                    num += 1
        return num        
    def checkSquare(self, matrix, startRow, startCol):
        firstRow = matrix[startRow][startCol: startCol+3]
        secondRow = matrix[startRow+1][startCol: startCol+3]
        thirdRow = matrix[startRow+2][startCol: startCol+3]
        
        _sum = sum(firstRow)
        _sum1 = sum(secondRow)
        _sum2 = sum(thirdRow)

        if _sum1 != _sum or _sum2 != _sum:
           return False
    
        ns = set(firstRow)
        ns.update(secondRow)
        ns.update(thirdRow)
        for x in self.all_nums:
            if not x in ns:
                return False
        
        if  matrix[startRow][startCol] +  matrix[startRow+1][startCol+1] + matrix[startRow+2][startCol+2] != _sum:
            return False
        if  matrix[startRow][startCol+2] +  matrix[startRow+1][startCol+1] + matrix[startRow+2][startCol] != _sum:
            return False  
        
        if matrix[startRow][startCol] + matrix[startRow+1][startCol] + matrix[startRow+2][startCol] != _sum:
            return False
        if matrix[startRow][startCol+1] + matrix[startRow+1][startCol+1] + matrix[startRow+2][startCol+1] != _sum:
            return False
        if matrix[startRow][startCol+2] + matrix[startRow+1][startCol+2] + matrix[startRow+2][startCol+2] != _sum:
            return False

        
        return True
