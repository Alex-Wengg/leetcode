class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        newList = []
        y = 0
        for i in range((len(matrix))):
            sublist = []
            for j in range((len(matrix) -1),-1,-1):
                
                sublist.append(matrix[j][y])
            newList.append(sublist)
            y += 1
            
        for i in range((len(matrix))):
            matrix[i] = newList[i]