class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        ROWS, COLS = len(grid), len(grid[0])
        seen = defaultdict(int)
        for i in range(ROWS):
            for j in range(COLS):
                seen[grid[i][j]] += 1
        
        res = [0, 0]
        for n in range(ROWS * COLS + 1):
            if seen[n] == 2: res[0] = n
            if seen[n] == 0: res[1] = n
        return res
