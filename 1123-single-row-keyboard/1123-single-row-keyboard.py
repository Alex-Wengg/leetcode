class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        char_dict = { char: index for index, char in enumerate(keyboard)}
        count = 0
        prev = 0 
        for char in word:
            count += abs(char_dict[char] - prev)
            prev = char_dict[char]

        return count