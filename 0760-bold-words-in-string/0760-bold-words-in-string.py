class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        

        mark = [0] * len(s)

        for word in words:
            index = s.find(word)
            while index > -1:
                for i in range(index, index + len(word)):
                    mark[i] += 1
                index = s.find(word, index+1)

        i = 0
        bolding = False
        result = []
        while i < len(s):
            
            if mark[i] != 0:
                result.append("<b>")
                while i < len(s) and mark[i] != 0:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1
        return "".join(result)
                