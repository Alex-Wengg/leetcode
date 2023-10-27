class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = list(zip(heights, names))
        n.sort()

        return [name for h, name in n][::-1]
