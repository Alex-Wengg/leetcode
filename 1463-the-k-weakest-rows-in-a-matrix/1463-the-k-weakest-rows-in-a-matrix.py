class Solution:
    def kWeakestRows(self, matrix: List[List[int]], k: int) -> List[int]:
        
        result = []
        for i in range(len(matrix)):
            result.append([matrix[i].count(1), i])
        result.sort()

        result_ = []
        for count_, i in result:
            if len(result_) == k:
                return result_
            result_.append(i)
        return result_
