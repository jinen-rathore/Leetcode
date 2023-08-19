class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # for the recursive relation we can find the next element if we know
        # the prev by adding k
        # f(n) = f(n-1) + k
        # we do the mod to keep in range of n because we are sitting in a round table
        # f(n) = (f(n-1) + k) % n
        def helper(n, k):
            if n == 1:
                return 0
            return (helper(n-1, k) + k) % n
        # we do +1 in the end to convert 0 indexing to 1 based indexing 
        return helper(n, k) + 1


            
            