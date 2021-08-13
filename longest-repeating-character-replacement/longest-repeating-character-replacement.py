class Solution:
    def characterReplacement(self, str1: str, k: int) -> int:
        mapp = {}
        largest = 0
        result = 0
        start = 0 
        # try to extend the range [windowStart, windowEnd]
        for end in range(len(str1)):
            right = str1[end]


            if right not in mapp:
                mapp[right] = 0
            mapp[right] += 1 
            
            largest = max(largest, mapp[right])
            

            
            if (end - start + 1 - largest) > k:
                left = str1[start]
                
                start += 1 
                mapp[left] -=1

        return end - start + 1