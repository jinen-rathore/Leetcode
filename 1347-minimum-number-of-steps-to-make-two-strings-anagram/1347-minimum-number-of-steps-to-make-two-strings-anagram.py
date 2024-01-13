class Solution:
    def minSteps(self, s: str, t: str) -> int:
        h = collections.Counter(s)        
        res = 0
        for char in t:
            if h[char] and h[char] > 0:
                h[char] -= 1
            else:
                res += 1
        return res