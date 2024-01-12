class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v = set("aeiouAEIOU")
        a = b = 0
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] in v:
                a += 1
            if s[j] in v:
                b += 1
            i += 1
            j -= 1
        
        return a == b