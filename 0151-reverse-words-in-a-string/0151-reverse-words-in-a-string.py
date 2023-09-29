class Solution:
    def reverseWords(self, s: str) -> str:
        """
        # to remove unwanted spaces we split and then join using space " "
        s = " ".join(s.split())
        
        # spliting the string to array
        l = s.split(" ")
        
        # reversing and joining the to form the desired string
        l = " ".join(reversed(l))
        return l
        """
        
        s = " ".join(s.split())
        
        arr = s.split()
        
        l, r = 0, len(arr) - 1
        while l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return " ".join(arr)
        