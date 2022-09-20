class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # sliding window?
        # [i, j] range
            # DSA to store the info
                # sort the DSA but sort while tracking their index place as well
        
        if t < 0:
            return False
        bucket = {}
        bucketSize = t + 1
        
        for i in range(len(nums)):
            num = nums[i]
            
            if i - k > 0:
                quotient = nums[i-k-1] // int(bucketSize)
                del bucket[quotient]
            quotient = num // bucketSize
            
            check1 = (quotient-1 in bucket and (abs(bucket[quotient-1] - num) <= t))
            check2 = ( quotient+1 in bucket and (abs(bucket[quotient+1] - num) <= t))
            check3 = quotient in bucket
            
            if check1 or check2 or check3:
                return True
            bucket[quotient] = num
        return False
                            