class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        a = arr[0]
        b = arr[1]
        c = arr[2]
        for i in range(2, len(arr)):

            a = arr[i-2]
            b = arr[i-1]
            c = arr[i]
            check = [a, b, c]
            consect = len([ c for c in check if c % 2 == 1])
            if consect == 3:
                return True 
        return False
