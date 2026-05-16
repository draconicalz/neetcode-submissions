class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seenNums = []
            for num in row:
                if num in seenNums:
                    print("Row false")
                    return False
                if num != ".":
                    seenNums.append(num)
        
        colDict = defaultdict(list)
        for row in board:
            for numIndex in range(len(board)):
                if row[numIndex] in colDict[numIndex]:
                    print(colDict)
                    print("Col false")
                    return False
                if row[numIndex] != ".":
                    colDict[numIndex].append(row[numIndex])
                
        
        for i in range(3):
            for j in range(3):
                seenNums = []
                for h in range(0+(i*3), (1+i)*3):
                    for v in range(0+(j*3), (1+j)*3):
                        if board[h][v] in seenNums:
                            print("Square false")
                            return False
                        if board[h][v] != ".":
                            seenNums.append(board[h][v])
                
        return True

        
            

        