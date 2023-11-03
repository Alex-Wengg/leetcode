class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = []
        p = path.split("/")

        for n in p:
            if stack and n == "..":
                stack.pop()
            elif n and n != ".." and n != ".":
                stack.append(n)
        print(stack)
        if not(stack):
            return '/'
        
        while stack:
            res.append( "/" + stack.pop())
        
        return ''.join(res[::-1])