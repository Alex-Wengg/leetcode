class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        num = [ k for k, v in counter.items() if v == 1]
        return max(num) if num else -1