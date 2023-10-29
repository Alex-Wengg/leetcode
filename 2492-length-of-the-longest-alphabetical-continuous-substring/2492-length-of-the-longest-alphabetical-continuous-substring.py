class Solution:
    def longestContinuousSubstring(self, s: str) -> int:

        max_len = 1  # minimum length is always 1 for non-empty strings
        current_len = 1  # start with the first character

        for i in range(1, len(s)):

            current_len += 1 if ord(s[i])-1 == ord(s[i-1]) else -(current_len-1)
            max_len = max(max_len, current_len)

        return max_len
