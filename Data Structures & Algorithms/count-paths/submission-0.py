class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * n for _ in range(m)]

        for j in range(m - 1, -1, -1):
            for i in range(n - 1, -1, -1):
                if j == m - 1:
                    matrix[j][i] = 1
                    continue

                if i == n - 1:
                    matrix[j][i] = matrix[j + 1][i]
                    continue
                
                matrix[j][i] = matrix[j + 1][i] + matrix[j][i + 1]
        return matrix[0][0]
