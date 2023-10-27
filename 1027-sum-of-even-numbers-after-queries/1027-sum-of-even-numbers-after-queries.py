class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum = []
        even_ = sum([ num for num in nums if num % 2 == 0])

        for val, i in queries:
            new = nums[i] + val 

            if new  % 2 == 0 and nums[i] % 2 == 0:
                even_ += val

            if new  % 2 == 1 and nums[i] % 2 == 0:
                even_ -= nums[i] 

            if new  % 2 == 0 and nums[i] % 2 == 1:
                even_ += new

            if new  % 2 == 1 and nums[i] % 2 == 1:
                pass

            nums[i] = new
            even_sum.append(even_)
        return even_sum

