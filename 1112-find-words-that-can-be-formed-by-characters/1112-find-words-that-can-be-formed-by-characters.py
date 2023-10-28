class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        counter = collections.Counter(chars)
        count = 0

        for word in words:
            flag = 1
            char_counter = collections.Counter(word)
            for char, counting in char_counter.items():
                if char not in counter or counting > counter[char]:
                    flag = 0
            count += len(word) if flag else 0
        return count