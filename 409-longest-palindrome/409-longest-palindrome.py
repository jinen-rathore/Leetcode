class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        c = 0
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for k in d:
            if d[k] % 2 == 1:
                c += 1
            
        return len(s) - c + (c>0)
                