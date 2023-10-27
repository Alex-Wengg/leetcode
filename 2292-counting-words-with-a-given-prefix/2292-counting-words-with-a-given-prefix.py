class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        len_ = len(pref)
        count = 0 

        for word in words:
            if word[:len_] == pref:
                count += 1
        return count