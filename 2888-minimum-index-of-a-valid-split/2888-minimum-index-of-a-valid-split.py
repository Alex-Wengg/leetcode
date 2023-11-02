class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        

        n = len(nums)
        res = -1
        prefix_counter = Counter()
        suffix_counter = Counter(nums)
        
        # Find the dominant element in the entire array first
        dominant = max(suffix_counter, key=suffix_counter.get)

        for i in range(n - 1):
            prefix_counter[nums[i]] += 1
            suffix_counter[nums[i]] -= 1
            
            if  prefix_counter[dominant] * 2 > i + 1 and \
             suffix_counter[dominant] * 2 > n - i - 1:
                res = i
                break 

        return res