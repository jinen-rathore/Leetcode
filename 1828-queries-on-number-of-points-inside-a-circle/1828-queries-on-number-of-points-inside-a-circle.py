class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)
        
        for i, val in enumerate(queries):
            x,y,r = val
            for p1,p2 in points:
                if math.sqrt((y-p2)**2 + (x-p1) ** 2) <= r:
                    res[i] += 1
        return res