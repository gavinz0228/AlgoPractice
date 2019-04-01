class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[ None for j in range(n)] for i in range(n)]
        increase = True
        col = True
        top, bottom, left, right = 0,n-1,0,n-1
        r, c = 0, 0
        count = 1
        target = n**2 
        
        while count <= target:
            #increase col
            if increase and col:
                matrix[r][c] = count
                count += 1
                if c < right:
                    c += 1
                else:
                    top +=1
                    col = False
                    r += 1
            elif increase and not col:
                matrix[r][c] = count
                count += 1
                if r < bottom:
                    r += 1
                else:
                    right -= 1
                    col = True
                    increase = False
                    c -= 1
            elif not increase and col:
                matrix[r][c] = count
                count += 1
                if c > left:
                    c -= 1
                else:
                    bottom -= 1
                    col = False
                    r -= 1
            elif not increase and not col:
                matrix[r][c] = count
                count += 1
                if r > top:
                    r -= 1
                else:
                    left += 1
                    col = True
                    increase = True
                    c += 1
        return matrix
