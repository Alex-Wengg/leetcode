class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        result = []
        seen_ = set()
        for i in range(1, n):

            for j in range(i+1, n+1):
                if i/j in seen_:
                    continue
                seen_.add(i/j)
                result.append(str(i) + "/" + str(j))
        return result