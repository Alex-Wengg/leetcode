class Solution:
    def canPartitionKSubsets(self, nums, k):
        if not nums:
            return False

        n = len(nums)
        # Result array
        dp = [False] * (1 << n)
        total = [0] * (1 << n)
        dp[0] = True

        # Calculate sum of all array elements
        total_sum = sum(nums)
        # Sort the array
        nums.sort()

        # If total_sum is not divisible by k, we can't partition the array
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        # If the largest number is greater than the target sum, we can't partition
        if nums[-1] > target_sum:
            return False

        # Loop over power set
        for i in range(1 << n):
            if dp[i]:
                # Loop over each element to find subset
                for j in range(n):
                    # Set the j-th bit
                    temp = i | (1 << j)
                    if temp != i:
                        # If total sum is less than target store in dp and total array
                        if nums[j] <= (target_sum - (total[i] % target_sum)):
                            dp[temp] = True
                            total[temp] = nums[j] + total[i]
                        else:
                            break

        return dp[(1 << n) - 1]

    # Example usage:
    # print(can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4))  # True or False depending on the possibility

