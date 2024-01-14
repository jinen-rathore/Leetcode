class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        h1,h2 = {},{}
        
        for c in word1:
            if c in h1:
                h1[c] += 1
            else:
                h1[c] = 1
        for c in word2:
            if c in h2:
                h2[c] += 1
            else:
                h2[c] = 1
                
        n1,n2 = {}, {}
        
        for i in h1.values():
            if i in n1:
                n1[i] += 1
            else:
                n1[i] = 1
        for i in h2.values():
            if i in n2:
                n2[i] += 1
            else:
                n2[i] = 1
        
        return n1 == n2