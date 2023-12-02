class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # burte force approach
        # using 3 loops and calculating the difference
        count = 0
        
        for i in range(1, len(nums)-1):
            if nums[i] - diff in nums and nums[i] + diff in nums:
                count += 1
        return count