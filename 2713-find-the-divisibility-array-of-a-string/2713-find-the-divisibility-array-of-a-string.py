class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
        result = [0] * len(word)
        str_ = ""

        for i, n in enumerate(word):
            str_ += n
            str_ = int(str_) % m
            str_ = str(str_)
            result[i] = int(int(str_) % m == 0)
        return result