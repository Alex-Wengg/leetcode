class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        yn = n 

        result =  []

        for i in range(yn):
            result.append(nums[i])
            result.append(nums[i+yn])
        
        return result 