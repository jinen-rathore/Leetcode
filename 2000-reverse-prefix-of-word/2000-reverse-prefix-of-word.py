class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        ind = 0
        for i, char in enumerate(word):
            if char == ch:
                ind = i
                break
        for i in range(ind, -1, -1):
            res += word[i]
        for i in range(ind + 1, len(word)):
            res += word[i]
        print(res)
        return res
                