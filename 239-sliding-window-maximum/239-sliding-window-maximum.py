class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # got to know when to pop the prior highest value
        dq = []
        res = []
        
        for i in range(len(nums)):
            if len(dq) > 0 and dq[0] == i - k:
                dq.pop(0)
                
            while len(dq) > 0 and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            
            if i >= k-1:
                res.append(nums[dq[0]])
        return res