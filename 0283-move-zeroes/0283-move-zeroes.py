class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i, j = 0,0
        # while i < len(nums) and j < len(nums):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #     j += 1
        
        # using snowball method
        ss = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ss += 1
            elif ss > 0:
                # swap with the left most snowball
                nums[i - ss] = nums[i]
                nums[i] = 0
        return nums
        
        