class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # brute Force solution
        """
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)
        return res
        """
        
        # using Hashing
        d = {}
        res = []
        temp = sorted(nums)
        for i, n in enumerate(temp):
            if n not in d:
                d[n] = i            
        for i in nums:
            res.append(d[i])
        return res