class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        h = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []
        for word in words:
            morse = ""
            for char in word:
                morse += h[ord(char)-97]
            res.append(morse)
        return len(set(res))