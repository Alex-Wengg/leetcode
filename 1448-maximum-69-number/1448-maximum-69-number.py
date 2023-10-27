class Solution:
    def maximum69Number (self, num: int) -> int:
        
        str_ = list(str(num))

        for i in range(len(str_)):
            if str_[i] == '6':
                num_ = str_[:i] + ['9'] + str_[i+1:]
                return int(''.join(num_))
        return num