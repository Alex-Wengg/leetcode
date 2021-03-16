def recursion(result ,sublist, nums, start):
    result.append(sublist[:])
    for i in range(start, len(nums)): 
        sublist.append(nums[i])
        #did not expect this. the i + 1
        recursion(result,sublist,nums, i + 1)
        print(sublist)
        sublist.pop();     
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        result = []
        sublist = []
        recursion(result ,sublist, nums, 0) 
        return result   
