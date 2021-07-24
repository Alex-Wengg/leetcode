class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        squares = []
 

        for i in range(len(arr)):
            squares.append(arr[i]*arr[i])

        squares.sort()
        
        return squares