class Solution:
        def trap(self, height: List[int]) -> int:
            #variables
            waterLevel = []
            left = 0
            
            #for loops 
            for h in height:
                left = max(left, h) 
                waterLevel += [left] # over-fill it to left max height
            right = 0
            #another one 
            for i, h in reversed(list(enumerate(height))):
                
                right = max(right, h)
                print(waterLevel[i],right,h )

                waterLevel[i] = min(waterLevel[i], right) - h # drain to the right height

            return sum(waterLevel)