class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        i = 0
        j = 0 
        while i < len(s) and j < len(words):
            word_le = len(words[j])
            word_len = word_le  if word_le > 1 else word_le
            print(" s[i: word_len] ",  s[i:word_len+ i ])
            print(" i ",   i)

            if words[j] == s[i: word_len+ i ]:
                i += word_len
                j += 1
            else:
                return False

        return (i >= len(s))
