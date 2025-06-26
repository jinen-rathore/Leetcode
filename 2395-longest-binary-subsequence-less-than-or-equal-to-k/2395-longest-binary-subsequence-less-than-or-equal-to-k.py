class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ones = 0
        val = 0
        power = 1
        zeros = 0

        for i in range(len(s)):
            if s[i] == "0":
                zeros += 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                if val + power > k:
                    continue
                val += power
                ones += 1
            power <<= 1 # bit shift 1 or can be 2^power
            if power > k:
                break
        return zeros + ones
            