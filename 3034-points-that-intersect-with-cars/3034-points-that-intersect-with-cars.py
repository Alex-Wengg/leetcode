class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        seen_ = set()
        for x,y  in nums:
            for i in range(x, y+1):
                seen_.add(i)
        return len(seen_)