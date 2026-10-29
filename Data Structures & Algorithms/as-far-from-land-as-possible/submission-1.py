from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        N = len(grid)
        
        # get all 1 nodes then run multi source bfs
        hasZero = False
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append((r, c))
                    visited.add((r, c))
                else: hasZero = True
        
        if not hasZero: return -1 
        def invalid(r, c):
            if r < 0 or c < 0 or r == N or c == N or (r, c) in visited or grid[r][c] == 1: return True
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        depth = -1 # start at -1 because we are starting at the origins. first loop depth = 0, second loop depth = 1. expected behavior 
        while q:
            depth += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newR, newC = r + dr, c + dc
                    if invalid(newR, newC): continue
                    q.append((newR, newC))
                    visited.add((newR, newC))
        return depth
