class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
        rank_size = []
        for n in nums:
            n.sort()
            
        for i in range(len(nums[0])):
            max_val = max(row[i] for row in nums)  # Get max value of ith column
            rank_size.append(max_val)
        
        return sum(rank_size)