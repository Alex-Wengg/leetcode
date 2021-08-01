class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets= [[]]
        
        for curr in (nums):
            n = len(subsets)
            
            for i in range(n):
                
                s = list(subsets[i])
                s.append(curr)
                subsets.append(s)
        
        return subsets