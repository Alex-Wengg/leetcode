class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1: return False
        target = total / 2   #target sum 
        s = set([0])         #stores the sums of the subsets
        
       
        for n in nums:
            sums_with_n = []  #stores the sums of the subsets that contain n
            for i in s:
                if i + n == target: return True
                if i + n < target:
                    sums_with_n.append(i + n)
            s.update(sums_with_n)
            print(s)
        return False