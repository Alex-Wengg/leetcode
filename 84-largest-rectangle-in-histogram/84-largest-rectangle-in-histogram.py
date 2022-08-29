class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        resMax = 0 
        for i in range(len(heights)):
            
            while  heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                size = (i - stack[-1] - 1) * h
                resMax = max(size, resMax)
            
            stack.append(i)
        
        return resMax