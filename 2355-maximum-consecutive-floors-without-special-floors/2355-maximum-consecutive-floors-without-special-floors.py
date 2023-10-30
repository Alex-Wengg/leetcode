class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        set_ = set(special)

        sorted_ = sorted(list(set_)) 
        print(sorted_)

        max_ = 0 
        for i in range(1, len(sorted_)):
            max_ = max(max_, sorted_[i] - sorted_[i-1]-1 )
        return max([sorted_[0] - bottom, max_, top - sorted_[-1]])