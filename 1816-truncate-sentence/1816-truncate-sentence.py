class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l = s.split(" ")
        res = []
        for i in range(k):
            res.append(l[i])
        return " ".join(res)