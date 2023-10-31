class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        len_ = len(str(high)) - len(str(low))

        seq = "123456789"
        result = []
        for window_size in range(len(str(low)), len(str(high))+1):

            for i in range(len(seq) - window_size + 1):
                cut = seq[i: window_size + i]
                print(cut)
                if low <= int(cut) <= high:
                    result.append(int(cut))
        return result