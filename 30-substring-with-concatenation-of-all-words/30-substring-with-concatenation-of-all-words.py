from copy import deepcopy

class Solution:
    def findSubstring(self, str1: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0:
            return []
        result = []
        hashmap = {}
        for word in words:
            if word not in hashmap:
                hashmap[word] = 0
            hashmap[word] += 1
        wordSize = len(words[0])
        for i in range(len(str1) - wordSize * len(words) +1):
            checkRange = str1[i:i+wordSize]
            if checkRange in hashmap:
                can = 1
                j = i
                hashmap2 = deepcopy(hashmap)
                while hashmap2:
                    checkRange = str1[j :wordSize+j]
                    if checkRange not in hashmap2:
                        can = 0
                        print('check')
                        break
                    hashmap2[checkRange] -= 1
                    if hashmap2[checkRange] == 0:
                        del hashmap2[checkRange]
                    j +=  wordSize

                            

                if can:
                    result.append(i)
                        
        return result