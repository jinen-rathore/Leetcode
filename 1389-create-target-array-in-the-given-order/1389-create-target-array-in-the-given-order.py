class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     res.insert(index[i], nums[i])
        # return res
        
        # to keep the front and back same we use res[i:i]
        res = []
        for n,i in zip(nums, index):
            res[i:i] = [n]
        return res
    
        # example: 
        # res = [1,2,3]
        # res[1:1] = [a]
        # res becomes [1,a,2,3]
        
        
    
        