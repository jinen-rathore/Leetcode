class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # approach dp
        m = len(text1)
        n = len(text2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i+1][j] , dp[i][j+1])
        return dp[-1][-1]