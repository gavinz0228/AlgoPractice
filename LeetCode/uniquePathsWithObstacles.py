class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
        else:
            obstacleGrid[0][0] = -1
        
        for i in range(1, height):
            if obstacleGrid[i - 1][0] == -1 or obstacleGrid[i][0] == 1:
                obstacleGrid[i][0] = -1
            else:
                obstacleGrid[i][0] = 1

        for i in range(1, width):
            if obstacleGrid[0][i-1] == -1 or obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = -1
            else:
                obstacleGrid[0][i] = 1

        for i in range(1, height):
            for j in range(1, width):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                else:
                    top = obstacleGrid[i-1][j]
                    left = obstacleGrid[i][j-1]
                    if top > -1 :
                        obstacleGrid[i][j] += top
                    if left > -1:
                        obstacleGrid[i][j] += left
        goal = obstacleGrid[-1][-1]
        if goal == -1:
            return 0
        else: 
            return goal
