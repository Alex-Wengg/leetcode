class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        res = 0

        for i, n in enumerate(heights):

            while heights[stack[-1]] > heights[i]:
                pop_ = heights[stack.pop()]
                size = (i - stack[-1] - 1) * pop_
                res = max(size, res)
            stack.append(i)
        
        return res
            
 