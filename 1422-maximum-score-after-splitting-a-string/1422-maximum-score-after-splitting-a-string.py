class Solution:
    def maxScore(self, s: str) -> int:
        max_ = float("-inf")
        
        for i in range(1, len(s)):
            max_ = max(max_, s[:i].count("0") + s[i:].count("1"))
        return max_