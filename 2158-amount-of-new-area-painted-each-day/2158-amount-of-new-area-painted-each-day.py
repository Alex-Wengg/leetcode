class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        paintedWallUnit = {}
        res = []
        
        for start, end in paint:
            
            count = 0 
            while start < end:
                
                
                if start in paintedWallUnit:
                    prev_end = paintedWallUnit[start]
                    
                    paintedWallUnit[start] = max(paintedWallUnit[start], end )
                    start = prev_end
                else:
                    paintedWallUnit[start] = end
                    start += 1
                    count += 1
            res.append(count)
        return res