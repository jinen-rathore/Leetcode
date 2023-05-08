class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        d =  dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        
        output = ""
        for key, val in d.items():
            output += key*val
        return output