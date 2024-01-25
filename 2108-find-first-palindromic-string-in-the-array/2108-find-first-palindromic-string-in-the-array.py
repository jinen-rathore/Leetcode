class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        return ""