class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if i == ROWS - 1 and j == COLS - 1: continue
                
                if i == ROWS - 1:
                    grid[i][j] += grid[i][j + 1]
                    continue
                if j == COLS - 1:
                    grid[i][j] += grid[i + 1][j]
                    continue
                
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
        return grid[0][0]