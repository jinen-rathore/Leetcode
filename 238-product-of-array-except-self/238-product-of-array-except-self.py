class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        arr = [1]*len(nums)
        
        pre = 1
        post = 1
        
        for i in range(len(nums)):
            arr[i] = pre
            pre *= nums[i]
            
        for j in range(len(nums)-1, -1, -1):
            arr[j] *= post
            post *= nums[j]
            
        return arr
        
            