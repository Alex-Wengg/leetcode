class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        sum_ = 0
        for i in range(len(arr)  ):
            
            sum_ += arr[i]
            
            # Check if the current subarray has size k
            if i >= k - 1:
                # If the current subarray's average is greater than or equal to threshold, increase the count
                if sum_ / k >= threshold:
                    cnt += 1
                
                # Remove the first element of the subarray from the sum
                sum_ -= arr[i-k+1]
        return cnt

