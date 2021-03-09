class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            newHash={}
            for count, num in enumerate(nums):

                if num not in newHash:
                    newHash[target-num] = count
                else:
                    return [newHash[num], count]
