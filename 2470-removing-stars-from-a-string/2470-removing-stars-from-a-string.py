class Solution:
    def removeStars(self, s: str) -> str:
        s = s[::-1]

        result = ""        
        star_stack = []

        for i in range(len(s)):

            if s[i] == "*":
                star_stack.append(i)
            elif len(star_stack):
                star_stack.pop()
            else:
                result += s[i]
        return "".join(result)[::-1]