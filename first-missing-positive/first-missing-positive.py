class Solution:
# O(n) time
    def firstMissingPositive(self, nums):
        unique = set(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i]<0 or nums[i]>=len(nums):
                nums[i]=0
        small = 1
        if small in unique:
            for i in range(0,len(nums)+1):
                if i+1 not in unique:
                    return i+1
                
        return small