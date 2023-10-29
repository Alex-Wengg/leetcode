class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result_ = [0] * len(arr)
        min_ = float('-inf')
        

        for i in range(len(arr) - 2, -1, -1):
            min_ = max(min_, arr[i+1])
            result_[i] = min_

        result_[-1] = -1 
        return result_