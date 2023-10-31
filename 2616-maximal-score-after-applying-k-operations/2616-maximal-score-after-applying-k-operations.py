class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [ -n for n in nums]
        heapq.heapify(nums)
        cnt = 0

        while k > 0:
            pop_ = -heapq.heappop(nums)
            cnt += pop_
            k -= 1
            heapq.heappush(nums, -math.ceil(pop_/ 3))
        
        return cnt
