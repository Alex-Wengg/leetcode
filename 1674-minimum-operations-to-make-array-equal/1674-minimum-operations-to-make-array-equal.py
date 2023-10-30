class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr.append( 2 * i + 1)

        avg_ = sum(arr) / len(arr)

        left = 0
        right = len(arr) - 1
        cnt = 0
        while left < right:
            cnt += avg_ - arr[left]
            left += 1
            right -= 1
        return int(cnt)