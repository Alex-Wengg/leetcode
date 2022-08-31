class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        height = [0] * (len(matrix[0]) + 1)
        ans = 0 
        for row in matrix:
            stack = [-1]
            for i in range(len(matrix[0])):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            # how come col doesn't get out of bound
                # bc height[] length is + 1 and height[-1] will be 0
            for col in range(len(matrix[0]) + 1):
                # why no check if stack exist
                    # first loop this while loop will fail bc height[-1]=0
                while stack and height[stack[-1]] > height[col]:
                    h = height[stack.pop()]
                    w = col - stack[-1] - 1
                    ans = max(ans, h * w)
                    
                stack.append(col)
        return ans
