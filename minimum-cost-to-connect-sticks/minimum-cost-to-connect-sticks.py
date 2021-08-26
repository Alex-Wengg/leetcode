class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        while len(sticks) > 1:
            sticks.sort()
            
            first = sticks.pop(0)
            second = sticks.pop(0)
            third = first + second
            
            result += third
            
            sticks.append(third)
        return result 