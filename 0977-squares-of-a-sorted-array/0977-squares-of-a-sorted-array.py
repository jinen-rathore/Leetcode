class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [x**2 for x in nums]
        return sorted(res)