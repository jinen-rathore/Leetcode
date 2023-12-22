class Solution:
    def maxScore(self, s: str) -> int:
        max_ = float("-inf")
        
        for i in range(1, len(s)):
            c0, c1 = 0, 0
            l = s[:i]
            r = s[i:]
            
            for j in l:
                if j == "0":
                    c0 += 1
            for j in r:
                if j == "1":
                    c1 += 1
            max_ = max(max_, c0+c1)
        return max_