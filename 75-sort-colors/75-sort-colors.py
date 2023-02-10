class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        # In the solution we use 2 pointers approach
        # if the index at nums is equal to 0 then we swap to front
        # else if the index at nums is equal to 2 then we swap to end 
        if len(nums) == 0 or len(nums) == 1:
            return nums;
        start = 0
        end = len(nums) - 1
        index = 0
        
        while start < end and index <= end:
            if nums[index] == 0:
                nums[index] = nums[start]
                nums[start] = 0
                
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[index] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                index += 1
        