class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        h = [0] * 26
        for i in sentence:
            h[ord(i) - 97] += 1
        for i in h:
            if i == 0:
                return False
        return True