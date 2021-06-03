class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 1
        for i in nums:
            if i == smallest:
                smallest += 1;
        return smallest