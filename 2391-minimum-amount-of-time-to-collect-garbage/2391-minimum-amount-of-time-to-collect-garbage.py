class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        
        ps = [0] * (len(travel) + 1)
        for i in range(1, len(ps)):
            ps[i] = ps[i-1] + travel[i-1]
            
        #             G P M    G P M
        last, count = [0,0,0], [0,0,0]
        
        for i in range(len(garbage)):
            for char in garbage[i]:
                if char == "G":
                    last[0] = i
                    count[0] += 1
                if char == "P":
                    last[1] = i
                    count[1] += 1
                if char == "M":
                    last[2] = i
                    count[2] += 1
        for i in range(len(last)):
            res += ps[last[i]] + count[i]
        return res