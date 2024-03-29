from collections import defaultdict
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        solution = 0
        def gcd(a, b):
            if a != 0:
                return gcd(b % a, a)
            else: 
                return b
		    
        
        for i in range(len(points)):
            mapp = defaultdict(int)
            duplicate = 0
            maxx = 0 
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                deltaX = x2 - x1
                deltaY = y2 - y1
                
                if deltaX == 0 and deltaY == 0:
                    duplicate += 1
                    continue
                deltaGcd = gcd(deltaX, deltaY)
                dX = deltaX // deltaGcd
                dY = deltaY // deltaGcd
                # our refrained loop to increment
                mapp[(dX,dY)] += 1
                # with i loop x1 and x2 as the comparator 
                # check other comparator of j loop
                maxx = max(maxx, mapp[(dX,dY)])
            # +1 for because the j loop gives n-1 total increments
            solution = max(solution, maxx + duplicate + 1 )  
        return solution