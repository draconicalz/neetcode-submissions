class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posD = set() # r + c
        negD = set() # r - c

        res = 0
        board = [["."] * n for i in range(n)]

        def dfs(r):
            nonlocal res
            if r == n:
                copy = ["".join(row) for row in board]
                res += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in posD or (r - c) in negD:
                    continue
                
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."
        dfs(0)
        return res