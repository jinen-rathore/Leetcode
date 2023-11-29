class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        hashmap = [0]*len(nums)
        
        for i in nums:
            hashmap[i-1] += 1
        res = []
        for i in range(len(hashmap)):
            if hashmap[i] == 2:
                res.append(i+1)
        return res
        """
        
        res = []
        
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                res.append(abs(nums[i]))
            nums[abs(nums[i])-1] = -1*nums[abs(nums[i])-1]
        return res