class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0 
        right = len(nums) - 1
        cnt = 0 

        while left < right:
            sum_ = nums[left] +  nums[right]
            
            if sum_ > k:
                right -= 1
            elif sum_ < k:
                left += 1
            else:
                cnt += 1
                right -= 1
                left += 1
        return cnt