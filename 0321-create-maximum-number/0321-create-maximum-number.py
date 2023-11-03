class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def find_max(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(p1, p2):
            return [max(p1, p2).pop(0) for _ in range(len(p1) + len(p2))]

        ret = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                p1 = find_max(nums1, i)
                p2 = find_max(nums2, k - i)
                ret = max(ret, merge(p1, p2))
        return ret
