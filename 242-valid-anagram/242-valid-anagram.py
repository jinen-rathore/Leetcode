class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [*s]
        l1.sort()
        l2 = [*t]
        l2.sort()
        if l1 == l2:
            return True
        else:
            return False