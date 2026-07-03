class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        TOTAL = ROWS * COLS
        minR, minC = 0, 0
        maxR, maxC = ROWS - 1, COLS - 1

        res = []
        i, j = 0, 0
        curDir = [0, 1]
        while True:
            res.append(matrix[i][j])
            if len(res) == TOTAL:
                return res

            if curDir == [0, 1] and j == maxC:
                curDir = [1, 0]
                minR += 1
            elif curDir == [1, 0] and i == maxR:
                curDir = [0, -1]
                maxC -= 1
            elif curDir == [0, -1] and j == minC:
                curDir = [-1, 0]
                maxR -= 1
            elif curDir == [-1, 0] and i == minR:
                curDir = [0, 1]
                minC += 1

            i += curDir[0]
            j += curDir[1]
                
            

            