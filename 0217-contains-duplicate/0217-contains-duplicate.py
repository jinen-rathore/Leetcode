class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return (len(nums) != len(set(nums)))
        
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        print(freq)
        for index, val in freq.items():
            if val > 1:
                return True
        return False