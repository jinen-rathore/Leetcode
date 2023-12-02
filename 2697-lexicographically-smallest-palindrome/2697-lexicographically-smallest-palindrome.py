class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = list(s)
        i, j = 0, len(l) - 1
        
        while i < j:
            if l[i] != l[j]:
                l[i] = min(l[i], l[j])
                l[j] = l[i]
                i += 1
                j -= 1
            else:
                i += 1
                j -= 1
        return "".join(l)