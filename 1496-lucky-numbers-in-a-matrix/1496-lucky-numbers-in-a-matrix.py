class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = [0] * len(matrix)
        for i in range(len(matrix)):
            min_row[i] = min(matrix[i])

        for i in range(len(matrix[0])):
            max_col = float("-inf")

            for j in range(len(matrix)):
                max_col = max(max_col, matrix[j][i])
            for j in range(len(matrix)):
                if max_col == min_row[j] :
                    return [ min_row[j]]
            
        return []