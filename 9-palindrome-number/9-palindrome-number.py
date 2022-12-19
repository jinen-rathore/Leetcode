class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            rev = str(x)
            return int(rev[::-1]) == x
        elif x == 0:
            return True
        else:
            return False