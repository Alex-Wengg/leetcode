class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        hash_ = collections.defaultdict(int)

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):
                num_i = nums[i]
                num_j = nums[j]
                hash_[num_i * num_j] += 1 
        
        sum_ = 0
        for k, v in hash_.items():
            sum_ += v * (v - 1) // 2 if v > 1 else 0 
        return sum_  * 8