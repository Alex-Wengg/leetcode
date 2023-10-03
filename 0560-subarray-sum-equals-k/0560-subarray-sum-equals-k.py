class Solution:
    def subarraySum(self, arr: List[int],target: int) -> int:
        res, cumSums = 0,0
        prefixSums = { 0 : 1 }

        for n in arr:
            cumSums += n
            diff = cumSums - target

            res += prefixSums.get(diff, 0)
            prefixSums[cumSums] = 1 + prefixSums.get(cumSums, 0)
        return res
