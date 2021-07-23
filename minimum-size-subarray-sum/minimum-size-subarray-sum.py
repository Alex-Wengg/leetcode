class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] >= target:
            return nums[0]
        if len(nums) == 1 and nums[0] <= target:
            return 0
        result = 99999999999999999999
        curr = 0
        start = 0
        length = 0
        track = 99999999999999999999
        for end in range(len(nums)):
            curr += nums[end]
            length += 1
            print(curr)
            while curr >= target:
                result = min(result, length )
                track = curr
                curr -= nums[start]
                length -= 1
                start += 1
                
             
 
        if result == 99999999999999999999:    
            return 0
        
        return result