class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        if k > len(nums):  # If k is larger than the array, return 0
            return 0
        
        max_sum = 0
        current_sum = 0
        hash_ = defaultdict(int)
        
        for right in range(len(nums)):
            # Add the current element to the hash map and current sum
            hash_[nums[right]] += 1
            current_sum += nums[right]

            # If the window size exceeds k, remove the leftmost element
            if right >= k:
                hash_[nums[right - k]] -= 1
                if hash_[nums[right - k]] == 0:
                    del hash_[nums[right - k]]
                current_sum -= nums[right - k]

            # If the window size is k and the number of distinct elements is at least m
            if right >= k - 1 and len(hash_) >= m:
                max_sum = max(max_sum, current_sum)
        
        return max_sum
