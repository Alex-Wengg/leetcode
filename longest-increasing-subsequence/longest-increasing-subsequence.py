class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [ ]
        def binarySearch(value,nums):
            end = len(nums)-1
            start = 0
            
            while start <= end:
                mid =start + (end-start)//2
                
                
                if  nums[mid] < value:
                    start = mid+1
                elif value < nums[mid]:
                    end = mid-1
                else:
                    return mid
            return start
        
        for i in range(len(nums)):
            search = binarySearch(nums[i],result)
            if  len(result) ==0 or   search >= len(result):
                result.append(nums[i])
            else:
                result[search] = nums[i]
        return len(result)