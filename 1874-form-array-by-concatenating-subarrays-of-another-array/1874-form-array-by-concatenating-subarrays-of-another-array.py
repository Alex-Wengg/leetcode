class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
 
        for group in groups:
            l = len(group)
            found = False
            for i in range(len(nums)):
                if group == nums[i:i+l]:
                    found = True
                    nums = nums[i+l:]
                    break
            if found == False:
                return False
        return True