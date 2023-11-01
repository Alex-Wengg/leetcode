class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # This will hold tuples of (character, count)

        for char in s:
            # If the stack is not empty and the last character is the same as the current one,
            # increment the count.
            if stack and stack[-1][0] == char:
                stack[-1] = (stack[-1][0], stack[-1][1] + 1)
                # If the count reaches k, pop that character off the stack.
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # Otherwise, add the character with a count of 1 to the stack.
                stack.append((char, 1))

        # Construct the final string.
        return ''.join(char * count for char, count in stack)

# Example usage:
solution = Solution()
print(solution.removeDuplicates("deeedbbcccbdaa", 3))  # Output should be "aa"
