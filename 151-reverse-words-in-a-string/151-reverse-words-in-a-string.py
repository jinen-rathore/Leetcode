class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        l = s.split(" ")
        l.reverse()
        l = " ".join(l)
        return l
        