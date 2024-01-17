class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [ord(x) for x in s if x in "AEIOUaeiou"]
        
        vowels = sorted(vowels)
        
        new_s = list(s)
        res = ""
        i = 0
        for char in new_s:
            if char not in "aeiouAEIOU":
                res += char
            else:
                res += chr(vowels[i])
                i += 1
        return res
                
                
        