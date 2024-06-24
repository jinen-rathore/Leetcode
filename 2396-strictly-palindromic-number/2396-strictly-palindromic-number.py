class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        def numToBase(n: int, b: int):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n%b))
                n //= b
            return digits[::-1]
        
        def palindrome(l: list):
            i, j = 0, len(l)-1
            while i < j:
                if l[i] != l[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        base = 2
        while base <= n-2:
            converted_to_base_list = numToBase(n, base)
            res = palindrome(converted_to_base_list)
            
            if not res:
                return False
            base += 1
        return True