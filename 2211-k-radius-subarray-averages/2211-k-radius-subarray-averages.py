class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        # Initialize the result array with -1, which is the default value if the subarray is not valid
        avgs = [-1] * n
        
        # Calculate the initial window sum
        window_sum = 0
        for i in range(2 * k + 1):
            if i < n:
                window_sum += nums[i]
            else:
                break  # Break if the window extends beyond the array bounds
        
        # If the initial window is valid, set the average for the k-th element
        if 2 * k < n:
            avgs[k] = window_sum // (2 * k + 1)
        
        # Slide the window across the array and update the sums and averages
        for i in range(k + 1, n - k):
            # Remove the element going out of the window and add the new element coming into the window
            window_sum -= nums[i - k - 1]
            window_sum += nums[i + k]
            
            # Update the average for the current center of the window
            avgs[i] = window_sum // (2 * k + 1)
        
        return avgs
