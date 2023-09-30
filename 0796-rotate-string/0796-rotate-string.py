class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def rightRotate(s):
            firstEle = s[0]
            rem = s[1:]
            return rem + firstEle
        
        for i in range(len(s)):
            if s == goal:
                return True
            s = rightRotate(s)
        return False
        