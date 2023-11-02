class Solution:
    def halveArray(self, nums: List[int]) -> int:
        ogSum = sum(nums)
        sum_ = sum(nums)
        nums.sort()
        cnt = 0

        if len(nums) <= 1:
            return 1

        heaped = [ -n for n in nums]
        heapq.heapify(heaped)

        while sum_ > ogSum / 2:
            popped = heapq.heappop(heaped) / 2
            sum_ -= -popped
            heapq.heappush(heaped, popped)
            cnt += 1
        
        return cnt

        
