class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # creating a hashmap to keep the count of all characters
        hashmap = {}
        res = 0
        # creating left pointer that points to the start
        l = 0
        # the right pointer iterated over the stirng
        for r in range(len(s)):
            
            # increment the count of the element encountered and if not found return a default value of 0
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)    
            
            # checking the condition: (Window size - max frequency element) > k then 
            # decrement the count of that element and increment the left pointer
            while (r - l + 1) - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
            # else that the max of window size or res
            res = max(res, r - l + 1)
        
        return res
            
                