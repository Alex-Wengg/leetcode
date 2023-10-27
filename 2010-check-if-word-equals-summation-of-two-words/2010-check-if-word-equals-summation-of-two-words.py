class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        firstNum = int(''.join([ str(ord(char) - ord('a')) for char in firstWord]))
        secondNum = int(''.join([ str(ord(char) - ord('a')) for char in secondWord]))

        targetNum = int(''.join([ str(ord(char) - ord('a')) for char  in targetWord]))

        return (firstNum + secondNum ) == targetNum