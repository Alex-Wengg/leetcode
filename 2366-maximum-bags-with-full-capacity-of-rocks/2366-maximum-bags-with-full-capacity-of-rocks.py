class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        cnt = 0

        diff = []
        for x,y in zip(capacity, rocks):
            if x ==y:
                cnt += 1
            else:
                diff.append(x-y)
            
        diff.sort()
        for c in diff:
            if additionalRocks - c < 0:
                break 
            additionalRocks -= c
            cnt += 1


        return cnt