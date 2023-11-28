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
        
        # approach 2:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)
        