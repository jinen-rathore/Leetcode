class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return (len(nums) != len(set(nums)))

        a = len(nums)
        b = len(set(nums))

        if(a == b):
            return False
        else:
            return True