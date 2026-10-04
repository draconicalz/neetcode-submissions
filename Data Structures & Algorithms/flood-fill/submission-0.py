class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        def dfs(i, j):
            if image[i][j] == color: return
            orig = image[i][j]
            image[i][j] = color

            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i2, j2 in dirs:
                if i + i2 >= ROWS or j + j2 >= COLS or i + i2 < 0 or j + j2 < 0 or image[i + i2][j + j2] != orig: continue
                dfs(i + i2, j + j2)
        
        dfs(sr, sc)

        return image