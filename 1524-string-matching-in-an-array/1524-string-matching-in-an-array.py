class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        cnt = []
        for word in words:

            for other_word in words:
                if other_word != word and word in other_word:
                    cnt.append(word)
        return list(set(cnt))