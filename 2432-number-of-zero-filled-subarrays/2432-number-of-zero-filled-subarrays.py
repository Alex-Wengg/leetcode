class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        left = 0
        right = 0
        cnt = 0

        while left < len(nums):
            if nums[left] == 0:
                while right < len(nums) and nums[right] == 0:

                    right += 1
                    cnt += abs(right - left)
                left += abs(right - left )
            left += 1
            right += 1
        return cnt 