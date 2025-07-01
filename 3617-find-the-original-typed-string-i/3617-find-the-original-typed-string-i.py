class Solution:
    def possibleStringCount(self, word: str) -> int:
        i, j = 0, 1
        count = 0
        while j < len(word):
            if word[i] == word[j]:
                count += 1
                j += 1
            else:
                i = j
                j += 1
        return count + 1