class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if len(grid) == 1 and len(grid[0]) == 1: return grid[0][0]
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        pq = []
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        def checkAdjacentAndPush(pos):
            for direction in dirs:
                new = (pos[0] + direction[0], pos[1] + direction[1])
                if (new in visited or new[0] < 0 or new[0] > ROWS - 1 or
                    new[1] < 0 or new[1] > COLS - 1): continue

                value = grid[new[0]][new[1]]
                heapq.heappush(pq, [value, (new[0], new[1])])
        
        visited.add((0,0))
        checkAdjacentAndPush((0, 0))
        
        minDepth = grid[0][0]
        while True:
            depth, position = heapq.heappop(pq)
            
            if position in visited: continue
            if depth > minDepth:
                minDepth = depth
            if position[0] == ROWS - 1 and position[1] == COLS - 1:
                return minDepth
            visited.add(position)
            checkAdjacentAndPush(position)

