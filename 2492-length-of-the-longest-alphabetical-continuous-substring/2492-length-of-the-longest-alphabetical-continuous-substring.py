class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1  # minimum length is always 1 for non-empty strings
        current_len = 1  # start with the first character

        for i in range(1, len(s)):
            if ord(s[i])-1 == ord(s[i-1]):  # Check if the current character continues the alphabetical order
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1  # Reset the count if the order is broken

        return max_len
