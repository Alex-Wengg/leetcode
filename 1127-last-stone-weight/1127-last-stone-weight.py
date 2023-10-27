class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()

        while len(stones) > 1:
            s1 = stones.pop(-1)
            s2 = stones.pop(-1)
            stones.append(abs(s2 - s1))
            stones.sort()
        return stones[-1]