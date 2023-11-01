from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        prefix_sums = [0]
        for num in arr:
            prefix_sums.append(prefix_sums[-1] + num)

        # Helper function to calculate the sum of the array after replacements
        def calculate_sum(value):
            # Find the first element greater than the value using binary search
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] <= value:
                    left = mid + 1
                else:
                    right = mid
            # Sum of elements before the first greater element + replacement sum
            return prefix_sums[left] + value * (len(arr) - left)

        # Binary search for the best value
        left, right = 0, arr[-1]
        best_diff = float('inf')
        best_value = -1

        while left <= right:
            mid = (left + right) // 2
            current_sum = calculate_sum(mid)
            diff = abs(current_sum - target)

            if diff < best_diff or (diff == best_diff and mid < best_value):
                best_diff = diff
                best_value = mid

            if current_sum < target:
                left = mid + 1
            else:
                right = mid - 1

        return best_value
