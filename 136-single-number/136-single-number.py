class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        for key,value in freq.items():
            if value == 1:
                return key