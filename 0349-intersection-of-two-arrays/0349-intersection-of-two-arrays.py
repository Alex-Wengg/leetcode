class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        map = {i : 0 for i in nums1}
        for j in nums2:
            if j in map:
                res.append(j)
                del map[j] 
        
        return res