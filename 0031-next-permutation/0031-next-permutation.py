class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        dip = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                dip = i
                break
                
        if dip == -1:
            return nums.reverse()
        
        for i in range(n-1, dip, -1):
            if nums[i] > nums[dip]:
                nums[i], nums[dip] = nums[dip], nums[i]
                break
        
        nums[dip + 1:] = reversed(nums[dip + 1:])
        