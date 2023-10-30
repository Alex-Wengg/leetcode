class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        left = 0 
        right = len(nums) - 1
        cnt = 0 

        while left < right:
            sum_ = nums[left] +  nums[right]
            
            right -= 1 if sum_ >= k else 0
            left += 1 if sum_ <= k else 0
            cnt += 1 if sum_ == k else 0
        return cnt