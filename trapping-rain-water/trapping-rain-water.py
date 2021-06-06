class Solution:
        def trap(self, height: List[int]) -> int:
            rightList = []
            rightBig = 0
            leftList = []
            leftBig = 0 
            
            for l in height:
                leftBig = max(l, leftBig)
                leftList.append(leftBig)
            trapped= 0
            reverse =  height[::-1]
            for r in reverse:
                rightBig = max(r, rightBig)
                rightList.append(rightBig)
            rightList = rightList[::-1]
            
            
            i = 0
            for h in reverse:
                
                trapped += min(leftList[i], rightList[i]) - h
                i += 1
        
            return trapped
        