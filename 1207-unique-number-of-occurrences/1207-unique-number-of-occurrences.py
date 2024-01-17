class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for num in arr:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        return len(set(h.values())) == len(h.values())