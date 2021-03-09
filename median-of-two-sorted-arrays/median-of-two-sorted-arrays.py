class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        for i in range(len(nums1)):
            nums3.append(nums1[i])
        for i in range(len(nums2)):
            nums3.append(nums2[i])
        nums3.sort()
        if len(nums3)%2==0:
            return ((nums3[len(nums3)//2]+nums3[len(nums3)//2-1]))/2
        else:
            return nums3[len(nums3)//2]