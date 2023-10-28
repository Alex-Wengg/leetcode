class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix, suffix = 0, sum(nums)
        ans = []
        for x in nums:
            prefix += x
            ans.append(abs(prefix - suffix))
            suffix -= x 
        return ans