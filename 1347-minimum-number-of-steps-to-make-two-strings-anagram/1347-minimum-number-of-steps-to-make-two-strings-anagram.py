class Solution:
    def minSteps(self, s: str, t: str) -> int:
        h1,h2 = {}, {}
        for i in s:
            if i not in h1:
                h1[i] = 1
            else:
                h1[i] += 1
        for i in t:
            if i not in h2:
                h2[i] = 1
            else:
                h2[i] += 1
        
        res = 0
        for k, v in h2.items():
            if k not in h1:
                res += v
            else:
                if v > h1[k]:
                    res += v - h1[k]
        return res