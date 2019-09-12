class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix)
        num_layers =  int(width / 2)
        for l in range(num_layers):
            s = l
            e = width - l - 1
            matrix[s][s], matrix[s][e], matrix[e][e], matrix[e][s] =  matrix[e][s], matrix[s][s], matrix[s][e], matrix[e][e]
            #print(matrix[s][s+1:e])  #top
            #print([ matrix[i][e] for i in range(s+1, e) ]) #right
            #print(matrix[e][s+1:e]) #bottom
            #print([ matrix[i][s] for i in range(s+1, e) ]) #left

            top = matrix[s][s+1:e]
            bottom = matrix[e][s+1:e]            
            matrix[s][s+1:e] = [ matrix[i][s] for i in range(e-1, s, -1) ]
            matrix[e][s+1:e] = [ matrix[i][e] for i in range(e-1, s, -1) ]
            for i in range(s+1, e):
                matrix[i][e] = top[i - s - 1]
                matrix[i][s] = bottom[i - s - 1]
