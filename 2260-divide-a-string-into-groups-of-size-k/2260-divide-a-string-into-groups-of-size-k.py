class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        g = (len(s) + k - 1) // k
        
        for i in range(g):
            t = ""
            for j in range(k):
                index = i * k + j
                if index < len(s):
                    t += s[index]
                else:
                    t += fill
            res.append(t)
        return res
