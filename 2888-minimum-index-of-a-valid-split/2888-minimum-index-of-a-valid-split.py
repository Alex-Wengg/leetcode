class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        

        n = len(nums)
        res = -1
        prefix_counter = Counter()
        suffix_counter = Counter(nums)
        
        # Find the dominant element in the entire array first
        dominant = max(suffix_counter, key=suffix_counter.get)

        for i in range(n - 1):
            # Move the current number from suffix to prefix
            prefix_counter[nums[i]] += 1
            suffix_counter[nums[i]] -= 1
            
            # If this element is no longer in the suffix, remove it
            if suffix_counter[nums[i]] == 0:
                del suffix_counter[nums[i]]
            
            # Check if the dominant element is the same for the prefix and suffix
            # And whether it meets the frequency requirements
            if (nums[i] == dominant or nums[i+1] == dominant) and \
                    prefix_counter[dominant] * 2 > i + 1 and \
                    suffix_counter[dominant] * 2 > n - i - 1:
                # Update result to the current index if all conditions are met
                res = i
                break  # We can break early since we only need the first valid split

        return res
