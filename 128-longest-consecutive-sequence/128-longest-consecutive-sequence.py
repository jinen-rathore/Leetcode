class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first create a set of the nums list
        s = set(nums)
        longest = 0
        
        # check if the number - 1 is in set or not 
        # for finding the sequece we check that n-1 is in set or not 
        
        for n in nums:
            if (n-1) not in s:
                length = 0
                while (n+length) in s:
                    length += 1
                longest = max(length, longest)

        return longest