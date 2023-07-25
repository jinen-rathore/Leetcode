class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = 3
        count = 0
        while j <= len(s):
            if len(set(s[i:j])) == 3:
                count += 1
            i += 1
            j += 1
        return count