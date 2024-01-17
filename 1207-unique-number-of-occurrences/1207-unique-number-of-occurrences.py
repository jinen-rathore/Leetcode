class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = {}
        for num in arr:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        l = [x for x in h.values()]
        return len(set(l)) == len(l)