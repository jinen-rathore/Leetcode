class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                
        # approach 2
        # we find if target - num is present in nums
        # if yes then we return the index of both
        
        checker = {}
        for i, v in enumerate(nums):
            if target - v in checker:
                return [checker[target - v], i]
            else:    
                checker[v] = i
        return []       
    
        # Brute Force Solution
        """
        arr = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append(i)
                    arr.append(j)
        return arr
        """
                
        
                    