class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1 
        if nums[start] < nums[end]:
            return nums[start]
        if start == end:
            return nums[start]
        mid =  (start+end)//2

        while start < end:
            
          
            if mid > 0 and mid < len(nums)-1 and nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if mid < len(nums)-1 and nums[mid] > nums[mid+1]:            
                return nums[mid+1]
            
            if nums[start] < nums[mid]:
                start = mid + 1
            elif nums[mid] < nums[end]:
                end = mid - 1
            mid = (start+end)//2
        return start                