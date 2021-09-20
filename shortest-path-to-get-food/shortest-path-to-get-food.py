from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        queue = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "*":
                    queue.append([row, col])
                    break
        
        paths = [[0,1], [1,0], [-1,0],[0,-1]]
        currentStep = 0
        seen = set()
        while queue:            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                seen.add((row, col))
                if grid[row][col] == '#':
                    return currentStep
                
                for dx, dy in paths:
                    nextRow = row + dx
                    nextCol = col + dy
                    
                    if 0 <= nextRow < rows and 0 <= nextCol < cols:
                        if grid[row][col] != 'X' and (nextRow,nextCol) not in seen:
                            seen.add((nextRow,nextCol))

                            queue.append([nextRow, nextCol])
            currentStep += 1
            
        return -1 