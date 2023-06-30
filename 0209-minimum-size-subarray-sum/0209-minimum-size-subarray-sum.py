class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
        window_start, longest, window_length = 0, len(nums)*len(nums), 0
        curr_sum = 0 

        left = 0
        for right in range(len(nums)):
            num = nums[right]
            curr_sum += num
            if curr_sum >= target:
                # longest = min(longest, right - left +1 )
                while curr_sum  >= target:
                    curr_sum -= nums[left]
                    left += 1
                longest = min(longest, right - left +2 )

        return longest if longest != len(nums)*len(nums) else 0