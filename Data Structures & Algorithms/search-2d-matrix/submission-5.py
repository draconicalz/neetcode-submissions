class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            mid = (l + r) // 2

            col = mid // len(matrix[0])
            row = mid % len(matrix[0])
            midNum = matrix[col][row]
            
            if midNum == target:
                return True
            elif midNum < target:
                l = mid + 1
            elif midNum > target:
                r = mid - 1
        
        return False
