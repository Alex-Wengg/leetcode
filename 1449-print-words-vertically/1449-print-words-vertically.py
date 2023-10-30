class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        list_s = s.split(" ")

        result = []
        for i in range(len(max(list_s, key=len))):
            tmp = ""
            for word in list_s:
                tmp += word[i] if i < len(word) else " "
            result.append(tmp.rstrip())
        return result 