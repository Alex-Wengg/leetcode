class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)

        digit_sum = 0
        for n in nums:
            for d in str(n):
                digit_sum += int(d)
        
        return element_sum - digit_sum