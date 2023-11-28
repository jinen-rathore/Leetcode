class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        # approach 1:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] - i != 0:
                return i
        return len(nums)
        """
        """
        # approach 2:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
        """
        
        # approach 3 using XOR
        res = 0
        for i in range(len(nums) + 1): # creating the full list ex for [3,0,1] full list is [0,1,2,3]
            res ^= i
        
        for i in nums:
            # we xor with the given list of numbers
            # the similar numbers with the xor present will cancel 
            # ex [0,1,2,3] ex => res = 0 ^ 1 ^ 2 ^ 3
            # in this step res = 0 ^ 1 ^ 2 ^ 3 ^ 0 0and0 will cancel
            # in the end only 2 will be left unpaired
            res ^= i
        return res