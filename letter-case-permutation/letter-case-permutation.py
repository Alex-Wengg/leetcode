class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = [s]
        
        for i in range(len(s)):
            if s[i].isalpha():
                n = len(permutations)
                for j in range(n):
                    new = list(permutations[j])
                    new[i] = new[i].swapcase()
                    permutations.append("".join(new))
        return permutations