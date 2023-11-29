class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force solution O(N^2) Gives TLE
        # to optimize that we will use the pre-computation.
        n = len(nums)
        p = [0] * n
        s = [0] * n
        
        # precomputing prefix 
        # ex for [1,2,3,4]
        # prefix will be => [1,1,2,6]
        px = 1
        for i in range(n):
            p[i] = px
            px *= nums[i]
        
        # precomputing suffix
        # ex for [1,2,3,4]
        # suffix will be => [24,12,4,1]
        sx = 1
        for i in range(n-1, -1, -1):
            s[i] = sx
            sx *= nums[i]
        
        # result will be the multiplication of corrosponding elements
        return [p[i]*s[i] for i in range(n)]
        