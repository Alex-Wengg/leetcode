class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        set_ = set()
        left = 0
        sum_ = 0
        tmpSum = 0

        for right, x in enumerate(nums):
            tmpSum += nums[right]
            

            while right - left +1 > k or x in set_:
                set_.remove(nums[left])
                tmpSum -= nums[left]
                left += 1
            set_.add(x)

            if  right - left +1 == k:
                sum_ = max(sum_, tmpSum)

        return sum_