class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_index = []
        for i, num in enumerate(nums):
            if num == key:
                key_index.append(i)
        
        res = set()
        for i in range(len(nums)):
            for keys in key_index:
                if abs(i - keys) <= k:
                    res.add(i)
        return list(res)