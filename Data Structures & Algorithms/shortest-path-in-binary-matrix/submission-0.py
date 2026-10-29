class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        N = len(grid)
        if N == 1: return 1
        q = deque([(0, 0)])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        visited = set([(0, 0)])
        
        def invalid(r, c):
            if r < 0 or c < 0 or r == N or c == N or grid[r][c] == 1 or (r, c) in visited: return True
        
        depth = 1
        while q:
            depth += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if invalid(newR, newC): continue
                    if newR == N - 1 and newC == N -1: return depth
                    q.append((newR, newC))
                    visited.add((newR, newC))
            
                    
        return -1