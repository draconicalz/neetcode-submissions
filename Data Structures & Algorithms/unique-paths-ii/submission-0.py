class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * COLS for n in range(ROWS)]
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                if i == ROWS - 1 and j == COLS - 1:
                    dp[i][j] = 1
                    continue
                if i == ROWS - 1:
                    dp[i][j] = dp[i][j+1]
                    continue
                if j == COLS - 1:
                    dp[i][j] = dp[i+1][j]
                    continue
                
                dp[i][j] = dp[i+1][j] + dp[i][j+1] 
        
        return dp[0][0]