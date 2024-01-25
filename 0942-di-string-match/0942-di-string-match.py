class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        l, r = 0, len(s)
        if s[0] == "D":
            res.append(r)
            r -= 1
        else:
            res.append(l)
            l += 1
            
        for i in range(1, len(s)):
            if s[i] == "I":
                res.append(l)
                l += 1
            elif s[i] == "D":
                res.append(r)
                r -= 1
        if s[-1] == "I":
            res.append(l)
        else:
            res.append(r)
        return res
        