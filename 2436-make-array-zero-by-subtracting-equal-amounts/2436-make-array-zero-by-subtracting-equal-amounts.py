class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 if nums[0] != 0 else 0 
        

        cnt = 0
        nums = [ n for n in nums if n > 0 ]
        if len(nums) == len(set(nums)):
            return len(nums)
        while nums:
            min_ = min(nums)
            nums = [ n for n in nums if n - min_ > 0 ]
            cnt += 1
        return cnt  