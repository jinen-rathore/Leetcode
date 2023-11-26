class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j = 0,n
        res = []
        while i < n and j < len(nums):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res