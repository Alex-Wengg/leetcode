class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        dx,dy = 0,1
        
        for step in instructions:
            if step == 'G':
                x ,y = x+dx, y+dy
            elif step == 'L':            
                dx, dy = -1*dy, dx
            else:
                dx, dy = dy, -1*dx

        return (x,y) == (0,0)or (dx,dy) != (0,1)