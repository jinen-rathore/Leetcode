class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # creating 2 pointers one left starting from 0 index and one right strarting from 1
        l, r = 0, 1
        
        # till right >= left and r not equal to end
        while l <= r and r != len(nums):
            
            # if the numbers are not equal we need to swap the location 
            if nums[l] != nums[r]:
                nums[l + 1] = nums[r]
                l += 1
            # if they are same just keep scaning till we get a mismatch and then swap with the next element of left pointer 
            else:
                r += 1
        return l + 1