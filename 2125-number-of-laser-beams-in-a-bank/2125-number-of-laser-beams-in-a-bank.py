class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ones = []
        
        for row in bank:
            if row.count("1") > 0:
                ones.append(row.count("1")) 
        
        beams = 0
        for i in range(len(ones)-1):
            beams += ones[i] * ones[i+1]
        return beams