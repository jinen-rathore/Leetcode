class Solution:
    def frequencySort(self, s: str) -> str:
        # creating a hashmap and storing the frequencies 
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        # reverse sorting the formed dictionary
        d =  dict(sorted(d.items(), key=lambda x:x[1],reverse=True))
        
        # appending the output to empty string as the number of frequency of occuring 
        output = ""
        for key, val in d.items():
            output += key*val
        return output