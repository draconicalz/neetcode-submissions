from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        length = len(board)
        
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r , c]
            
        q = deque() # square, steps
        q.append([1, 0])
        visited = set()
        while q:
            square, steps = q.popleft()
            
            for i in range(1, 7):
                next = square + i
                r, c = intToPos(next)
                if board[r][c] != -1:
                    next = board[r][c]
                if next == length * length:
                    return steps + 1
                if next not in visited:
                    visited.add(next)
                    q.append([next, steps + 1])
        return -1
