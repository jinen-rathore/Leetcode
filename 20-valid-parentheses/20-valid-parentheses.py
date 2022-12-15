class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
            elif len(stack) == 0 or d[stack.pop()] != char:
                return False
        return len(stack) == 0
                    
            