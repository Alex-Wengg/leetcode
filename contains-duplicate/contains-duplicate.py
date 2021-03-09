class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        thisset = set()
        for i in nums:
            if (i in thisset):
                return True
            thisset.add(i)
        return False