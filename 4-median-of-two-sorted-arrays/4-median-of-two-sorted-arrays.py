class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #r1, l1 from list1 
        #r2, l2 from list2
        # find r1 < l2 && r2 < l1 to find the median
        # we can measure accuracy using m1 = (r1+l1)/2
        # m2 = (len(list1) + len(list2)) - m1 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        start  = 0
        end = len(nums1)
        m, n = len(nums1), len(nums2)
        
        left_size = (m + n + 1) // 2
        while start <= end:
            a_part = (start + end)//2
            mid2 = left_size - a_part 
            
            aleftmax  = float('-inf') if a_part  == 0          else nums1[a_part  - 1]
            arightmin = float(' inf') if a_part  == len(nums1) else nums1[a_part ] 
            bleftmax  = float('-inf') if mid2 == 0          else nums2[mid2 - 1] 
            brightmin = float(' inf') if mid2 == len(nums2) else nums2[mid2] 

            if (aleftmax >brightmin ): # too far right on list1
                end = a_part  - 1
            elif (bleftmax > arightmin ):
                start = a_part  + 1
            else:
                if ((len(nums1) + len(nums2))%2) != 0:
                    return max(aleftmax ,bleftmax ) 

                return (max(aleftmax ,bleftmax ) + min(arightmin ,brightmin )) / 2
        return 0