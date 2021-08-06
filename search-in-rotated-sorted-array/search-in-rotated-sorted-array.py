class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
    
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1