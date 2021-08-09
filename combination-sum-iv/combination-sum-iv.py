class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dictt = { 0:1}
   
        for i in range(1,target+1 ):
            dictt[i] = 0
            for j in nums:
                if i - j >= 0:
                    dictt[i] += dictt.get(i - j , 0)
        return(dictt[target])   
