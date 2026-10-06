class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0

        for r in range(ROWS):
            rsum = sum(grid[r])
            if rsum < 2: continue

            res += rsum
            for c in range(COLS):
                if grid[r][c]: grid[r][c] = -1
        
        for c in range(COLS):
            col_sum = unmarked = 0
            for r in range(ROWS):
                col_sum += abs(grid[r][c])
                if grid[r][c] > 0:
                    unmarked += 1
                elif grid[r][c] < 0:
                    grid[r][c] = 1 # Unmark
            if col_sum >= 2:
                res += unmarked
        return res


        