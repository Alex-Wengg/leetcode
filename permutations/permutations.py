def permute(a, l, r, result):

    if l==r: 
        
        result.append(a[:]) 
        return 0
    
    for i in range(l,r+1): 
        a[l], a[i] = a[i], a[l] 
        permute(a, l+1, r, result) 
        a[l], a[i] = a[i], a[l]
class Solution(object):
    def permute(self, nums):
        n = len(nums) 
        result = []
        permute(nums, 0, n-1, result) 
        return result
 