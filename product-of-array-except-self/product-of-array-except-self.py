class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hasZero = False
        howManyZeroes = 0
        product = 1
        
        for i in nums:
            if i == 0:
                hasZero = True
                howManyZeroes += 1
            else:
                product *= i
        if howManyZeroes > 1:
            product = 0 
        for i in range(len(nums)):
            if hasZero == False:
                
                nums[i] = (product//nums[i])
            elif nums[i] != 0 and hasZero and howManyZeroes == 1:
                nums[i] = 0
            elif howManyZeroes > 1:
                nums[i] = 0
            elif nums[i] == 0:
                
                nums[i] = product
        return nums