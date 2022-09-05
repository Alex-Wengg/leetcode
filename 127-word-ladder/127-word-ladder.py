class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        transfPatt = dict()
        wordList.append(beginWord)
        for word in wordList:
            
            for i in range(len(word)):
                x = word[:i] + "*" + word[i+1:]
                if x not in transfPatt:
                    transfPatt[x] = []
                transfPatt[x].append(word)
        print(transfPatt)
        queue = [beginWord]
        res = 1
        seen = set(beginWord)

        while queue:
            for _ in range(len(queue)):
                first = queue.pop(0)
                if first == endWord:
                    return res            
                for i in range(len(first)):
                    x = first[:i] + "*" + first[i+1:]

                    for word in transfPatt[x]:
                        if word in seen:
                            continue
                        queue.append(word)
                        seen.add(word)
            res += 1
        return 0