class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        if len(matrix) == 0:
            return res
        rowStart = 0
        rowEnd = len(matrix)-1
        colStart = 0
        colEnd = len(matrix[0])-1
        
        while  rowStart <= rowEnd and colStart <= colEnd:
            for col in range(colStart, colEnd+1):
                res.append(matrix[rowStart][col])
            rowStart += 1

            
            for row in range(rowStart, rowEnd+1):
                res.append(matrix[row][colEnd])
            colEnd -= 1
            
            if rowStart <= rowEnd:
                for i in range(colEnd,colStart-1,-1):
                    res.append(matrix[rowEnd][i])
                rowEnd -=1
            
            if colStart <= colEnd:
                for row in range(rowEnd, rowStart-1, -1):
                    res.append(matrix[row][colStart])
                colStart +=1
            
        return res
            