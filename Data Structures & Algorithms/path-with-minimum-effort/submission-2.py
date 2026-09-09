class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        minq = [[0, (0, 0)]]
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        res = 0
        while minq:
            effort, cords = heapq.heappop(minq)
            res = max(effort, res)
            if cords == (ROWS - 1, COLS - 1): return res
            i, j = cords[0], cords[1]
            for i2, j2 in dirs:
                if i + i2 >= ROWS or i + i2 < 0 or j + j2 >= COLS or j + j2 < 0 or (i + i2, j + j2) in visited:
                    continue
                effort = abs(heights[i][j] - heights[i + i2][j + j2])
                heapq.heappush(minq, [effort, (i + i2, j + j2)])
                visited.add(cords)
                
        return res
