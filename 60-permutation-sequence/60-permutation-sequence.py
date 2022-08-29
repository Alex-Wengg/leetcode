import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = []
        factorials = [1] * n
        nums = list(map(str,range(1,10)))
        res = []
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            res.append(nums[index])
            nums.remove(nums[index])

        return "".join(res)