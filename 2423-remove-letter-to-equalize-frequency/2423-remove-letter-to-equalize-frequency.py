from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        
        for char in word:
            counter[char] -= 1
            
            if counter[char] == 0:
                counter.pop(char)
            
            if len(set(counter.values())) == 1:
                return True
            counter[char] += 1
        return False
            
        