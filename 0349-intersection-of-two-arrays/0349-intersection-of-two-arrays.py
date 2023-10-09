class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        map = {}
        for i in nums1:
            map[i] = map.get(i, 0) + 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        
        return res