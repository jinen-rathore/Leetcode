class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        r1, r2 = "", ""
        for c in word1:
            r1 += c
        for c in word2:
            r2 += c
        return r1 == r2