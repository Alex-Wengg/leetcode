class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()

        for x,y in zip(target, arr):
            if x != y:
                return False
        return True