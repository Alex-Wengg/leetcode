class Solution:
    def findSubstring(self, str1: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0:
            return []

        word_frequency = {}

        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 0
            word_frequency[word] += 1
        result_indices = []
        count = len(words)
        length = len(words[0])
        
        for i in range((len(str1) - count*length)+1):
            
            seen = {}
            
            for j in range(0, count):
                
                index = i + j * length 
                
                word = str1[index: index+length]
                
                if word not in word_frequency:
                    break
                
                if word not in seen:
                    seen[word] = 0
                seen[word] += 1
                
                if seen[word] > word_frequency.get(word, 0):
                    break
                
                if j+1 == count:
                    result_indices.append(i)
                    
        return result_indices