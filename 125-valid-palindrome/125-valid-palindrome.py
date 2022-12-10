class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [*s]
        nl = []
        for i in range(len(l)):
            if l[i].isalnum():
                nl.append(l[i].lower())
                
        return nl == nl[::-1]
                