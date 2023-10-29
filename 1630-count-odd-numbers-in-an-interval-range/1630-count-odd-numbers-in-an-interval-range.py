class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = 0
        low_ = low - 1 if low % 2 == 1 else low
        high_ = high + 1 if high % 2 == 1 else high 
        print((high_ - low_) // 2)
        return (high_ - low_) // 2 