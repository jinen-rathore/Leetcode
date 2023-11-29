class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap = [0]*len(nums)
        
        for i in nums:
            hashmap[i-1] += 1
        res = []
        for i in range(len(hashmap)):
            if hashmap[i] == 2:
                res.append(i+1)
        return res
            