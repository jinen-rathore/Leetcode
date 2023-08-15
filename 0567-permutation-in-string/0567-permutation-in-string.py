class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = len(s1)
        d = collections.Counter(s1)
        
        for i in range(len(s2) - l + 1):
            window = s2[i:i+l]
            
            if d == collections.Counter(window):
                return True
        return False
                
        
        