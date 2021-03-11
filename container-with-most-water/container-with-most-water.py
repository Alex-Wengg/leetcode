class Solution:
    def maxArea(self, height: List[int]) -> int:
        currArea= 0
        start = 0
        length =0
        end = len(height)-1
        while (start < end):
            length = min(height[start], height[end])
            currArea = max(currArea, length*(end-start))
            if height[start] > height[end]:
                end -= 1
            else:
                start +=1
                
        return currArea
        