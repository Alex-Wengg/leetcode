class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i-1 ] == nums[i]:
                nums[i-1] *= 2 
                nums[i] = 0

        zero_i = len(nums) - 1
        result = []
        for i in range( len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
        return result + [0] * nums.count(0)