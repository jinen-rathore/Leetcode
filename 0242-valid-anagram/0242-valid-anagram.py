class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # l1 = [*s]
        # l1.sort()
        # l2 = [*t]
        # l2.sort()
        # if l1 == l2:
        #     return True
        # else:
        #     return False
        
        if len(s) != len(t):
            return False
        
        hashmap = [0] * 26
        
        for char in s:
            hashmap[ord(char) - 97] += 1
        for char in t:
            hashmap[ord(char) - 97] -= 1
            if hashmap[ord(char) - 97] < 0:
                return False
        return True