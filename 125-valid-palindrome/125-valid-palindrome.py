class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # time complexity = O(N) using extra memory and built in functions
        # space complxity = O(N)
#         newStr = ""
#         for i in s:
#             if i.isalnum():
#                 newStr += i.lower()                
#         return newStr == newStr[::-1]
                
    # for beter approach using 2 pointers and without using isalnum()
    # time complxity = O(N) and space compexity = O(1)
        
        def alphaNum(ch):

            return ((ord('A') <= ord(ch) <= ord('Z')) or 
                    (ord('a') <= ord(ch) <= ord('z')) or 
                    (ord('0') <= ord(ch) <= ord('9')))
        l = 0
        r = len(s)-1

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while l < r and not alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True