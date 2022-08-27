class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        return self.solve(board, 0,0)
        
    def solve(self, board: List[List[str]], r, c) -> None:
        
        
        while board[r][c] != '.':
            c += 1
            if c == 9:
                c, r = 0, r+1

            if r == 9:
                return True
        
        for k in range(1,10):
            if self.check(board, r, c, str(k)):
                board[r][c] = str(k)
                if self.solve(board, r, c):
                    return True
        board[r][c] = '.'
        return False
                    
    
    def check(self, board, i, j, val):
        if i == 9 or j == 9:
            return False
        row = i - i % 3 
        col = j - j % 3
        
        for x in range(0, 9):
            if board[x][j] == val:
                return False
        
        for y in range(0,9):
            if board[i][y] == val:
                return False
        
        for x in range(0, 3):
            for y in range(0, 3):
                
                if board[x+row][y+col] == val:
                    return False
        return True
    