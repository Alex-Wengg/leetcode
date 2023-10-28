class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        

        for i in range(len(grid)):
            if grid[i][i] == 0:
                return False 

            if grid[len(grid)- i - 1][i] == 0:
                return False 

            grid[i][i] = 69
            grid[len(grid)- i - 1][i] = 69

        for i in grid:
            print(i)   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 69 or  grid[i][j] == 0:
                    pass 
                else:
                    return False

             
        
        return True
