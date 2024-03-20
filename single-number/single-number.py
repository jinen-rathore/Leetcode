class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # counting the ferquency of each element in the list
        # and storing them into a dictionary
        # then iterating the dictionary if the value == 1 then return the key
        # time complexity: O(N)
        freq = {}
        
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        for key,value in freq.items():
            if value == 1:
                return key