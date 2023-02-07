class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         if len(nums) == 0:
#             return [[]]
        
#         subset = []
        
#         first_ele = nums[0]
#         remaining_ele = nums[1:]
        
#         for partial_subset in self.subsets(remaining_ele):
#             subset.append(partial_subset)
#             subset.append(partial_subset + [first_ele])
#         return subset

        # Approach 2
        ret = [[]]
        for n in nums:
            ret += [r + [n] for r in ret]
        return ret
        
        