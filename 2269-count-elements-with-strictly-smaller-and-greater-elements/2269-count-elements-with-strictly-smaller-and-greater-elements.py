class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums)) <= 2:
            return 0

        min_ = min(nums)
        nums.sort()
        min_i = 0
        while nums[min_i] == min_:
            min_i += 1

        max_i = len(nums) -1 
        max_ = max(nums)
        while nums[max_i] == max_:
            max_i -= 1

        return len(nums[min_i:max_i]) +1