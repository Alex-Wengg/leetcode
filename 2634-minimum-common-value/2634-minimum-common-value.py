class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        c_ = set(nums1) & set(nums2)
        return min(c_) if c_ else -1