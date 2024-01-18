class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Time complexity: O(N)
        # We will use dp as to get to nth step if we get the (n-1)th step and (n-2)th step we can add those and get the answer
        # so essentily it converts to a fibb series problem
        if n == 1:
            return 1
        # using tabulation
        dp = [0] * (n+1)
        
        # we are the the first step => number is 1 
        dp[0] = 1
        # similarly to jump to second we only need one step
        dp[1] = 1
        
        for i in range(2,n+1):
            # after that to get to any other step we need 
            # the sum on previous 2 steps as we can only jump 1 or 2 steps
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]