class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negatives = 0 
        
        if len(nums) == 1:
            return  (nums[0] )
        
        maxx = 0
        result = 0
        minn = 0
        for x in range(len(nums)):
            i = nums[x]
            temp =   maxx*i
            maxx = max(minn*i,temp, i)
            minn = min(minn*i, temp, i)

            result = max(result, maxx)
        return result