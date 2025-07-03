class Solution:
    def kthCharacter(self, k: int) -> str:
        n = 1
        word = "a"
        while k >= n:
            t = ""
            for char in word:
                t += chr(ord(char) + 1)
            word += t
            n *= 2
        print(word)
        return word[k-1]