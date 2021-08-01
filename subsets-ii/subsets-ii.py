class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets= [[]]
        prev = 0 
        nums.sort()
        for i in range(len(nums)):
            n = len(subsets)
            start =  0
            if i > 0 and nums[i-1] == nums[i]:
                start = prev+1
            for j in range(start, n):
                
                s = list(subsets[j])
                s.append(nums[i])
                subsets.append(s)
            prev = j
        return subsets