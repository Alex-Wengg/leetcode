class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for i in range(0, len(s)):

            if not(stack) or stack[-1][0] != s[i]:
                stack.append([s[i], 1])
            
            else:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
        
        return ''.join(char * count for char, count in stack)
