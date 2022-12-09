class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in set(nums):
            counts[i] = nums.count(i)
                
        arr = sorted(counts,key = counts.get, reverse = True)
        return arr[:k]
        
        