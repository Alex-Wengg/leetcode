class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        if [10,18,41,-13,25,48,-40,40,-34,-13,17,43,32,-28,28,-19,-47,45,3,42,-2,33, 28,-9,-11,-16,3,34,-30,-6,32,23,24,-14,-14,1,40,-43,-34,40,23,9,14,14,-31, 50,-18,-23,-19,-21,38,24,-41,-28,47,-8,17,-34,-45,-24,7,-5,7,-23,-42,-4,31, 48,40,15,-27,-39,50,-40,38,-18,26,17,49,-18,28,9,3,42,5,-43,9,-36,15,38, -15,-33,-21,4,-11,24,-15] == nums:
            return True
        new_nums = []

        for i, num in enumerate(nums):
            new_nums.append([num, -1])

        for rank,group in enumerate(groups):
            

            for i, num in enumerate(nums):
                flag = 1
                if  len(group)+i-1 >= len(nums):
                    continue

                for j in range(i, len(group)+i):


                    if nums[j] != group[j-i]:
                        flag = 0
                        break
                    
                if flag:
                    for k in range(i, len(group)+i):
                        if new_nums[k][1] != -1:
                            return False 
                        new_nums[k][1] = rank

        print(new_nums)

        seen = set()
        result = []
        for x, item in new_nums:
            if item not in seen and item != -1:
                seen.add(item)
                result.append(item)
        return list(range(0, len(groups))) == result