class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        result = []
        for word in words:
            result.extend(filter(lambda x: x, word.split(separator)))
        return result 