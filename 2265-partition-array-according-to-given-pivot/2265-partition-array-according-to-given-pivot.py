class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot = []
        pivot_num = []
        great_pivot = []
        for num in nums:
            if num < pivot:
                less_pivot.append(num)
            elif num > pivot:
                great_pivot.append(num)
            else:
                pivot_num.append(num)
        pivot_num.extend(great_pivot)
        less_pivot.extend(pivot_num)
        return less_pivot