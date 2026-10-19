class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
        for x, y in dirs:
            curLen = 1
            curR, curC = rMove, cMove

            nextR, nextC = curR + x, curC + y
  
            if not (0 <= nextR < ROWS and 0 <= nextC < COLS):
                continue

            if board[nextR][nextC] in [".", color]:
                continue

            while True:
                curR += x
                curC += y
                if curR >= ROWS or curC >= COLS or curR < 0 or curC < 0 or board[curR][curC] == ".":
                    break

                if board[curR][curC] == color:
                    curLen += 1
                    if curLen >= 3:
                        return True
                    break

                curLen += 1
        return False
