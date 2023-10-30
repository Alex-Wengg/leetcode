class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        set_a = set()
        set_b = set()
        result = []

        for x,y in zip(A, B):
            set_a.add(x)
            set_b.add(y)   
            result.append(len(set_a & set_b))
        return result 