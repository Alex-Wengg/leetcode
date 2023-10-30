class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        max_range = [n for n in nums]

        for i in range(1, len(nums)):
            max_range[i] = max(nums[i], max_range[i-1])
        
        nums[0] += max_range[0]
        for i in range(1,  len(nums)):
            nums[i] +=  max_range[i] + nums[i-1]
        return nums