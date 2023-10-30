class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        sum_ = 0
        for i in range(len(arr)  ):
            
            sum_ += arr[i]
            cnt += sum_ / k >= threshold and i -k + 1 >= 0

            if i -k + 1 >= 0:
                sum_ -= arr[i-k+1]

        return cnt

