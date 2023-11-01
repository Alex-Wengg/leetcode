class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor):
            return sum(ceil(num / divisor) for num in nums)
        
        # Binary search
        left, right = 1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if compute_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid - 1
        
        return left