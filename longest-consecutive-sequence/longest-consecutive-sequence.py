class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0 
        for n in nums:
            if n -1 not in s:
                count = 1
                while n + 1 in s:
                    count += 1 
                    n+= 1 
                ans = max(ans, count)
        return ans 