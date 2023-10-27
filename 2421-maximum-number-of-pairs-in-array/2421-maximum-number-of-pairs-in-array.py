from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        even_sets = 0
        odd_sets = 0
        for key, value in counter.items():
            even_sets += value // 2
            odd_sets += value % 2
        
        return [even_sets, odd_sets]