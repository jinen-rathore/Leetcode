class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return [nums]
        else:
            l = []
            for i in range(len(nums)):
                # taking current element
                m = nums[i]
                
                # Fixing one element and swaping the remaining 2 for permutations
                remList = nums[:i] + nums[i+1:]
                
                for p in self.permute(remList):
                    l.append([m] + p)
            return l