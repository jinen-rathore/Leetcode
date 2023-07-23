class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # we create a result array with all 1 in it to store the prefix and postfix and reduce the time complexity
        res = [1] * len(nums)
        
        # starting with prefix = 1 means the product of elements before that particular element
        prefix = 1
        # same with posrfix = 1 product of elements after that particular element
        postfix = 1
        
        # we compute the prefix by first putting the prefix into element's place then multiplying it with the element after that
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # similirly we compute the postfix
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        
        