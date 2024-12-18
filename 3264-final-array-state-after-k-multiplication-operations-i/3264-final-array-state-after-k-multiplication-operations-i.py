import heapq as hq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [[num,i] for i, num in enumerate(nums)]
        
        hq.heapify(min_heap)
        while k:
            min_heap[0][0] *= multiplier
            hq.heapify(min_heap)
            
            k -= 1
        for num, index in min_heap:
            nums[index] = num
        return nums