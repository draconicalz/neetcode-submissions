class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        lengthMat = [[0] * COLS for _ in range(ROWS)]
        globalMax = 0

        def dfs(i, j):
            if lengthMat[i][j] != 0: return lengthMat[i][j]

            length = 1
            for dirs in directions:
                new = (i + dirs[0], j + dirs[1])
                if new[0] >= ROWS or new[1] >= COLS or new[0] < 0 or new[1] < 0: continue
                
                if matrix[new[0]][new[1]] > matrix[i][j]:
                    length = max(length, dfs(new[0], new[1]) + 1)
            
            lengthMat[i][j] = length
            return length
        
        for i in range(ROWS):
            for j in range(COLS):
                globalMax = max(globalMax, dfs(i, j))
        print(lengthMat)
        return globalMax
                

            

