class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        set_ = set(nums)

        for n in nums:
            n = str(n)[::-1]
            set_.add(int(n))
        return len(set_)