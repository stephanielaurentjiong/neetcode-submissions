class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dictionary = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if stack and stack[-1] == dictionary.get(char):
                    stack.pop()
                else:
                    return False
    
        return True if not stack else False