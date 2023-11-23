class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # checker = {}
        # for i, v in enumerate(nums):
        #     if target - v in checker:
        #         return [checker[target - v], i]
        #     else:    
        #         checker[v] = i
        # return []       
        
        arr = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append(i)
                    arr.append(j)
        return arr
                    