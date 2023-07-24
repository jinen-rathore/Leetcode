class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        l = 0
        
        for r in range(len(s)):
            # element not seen then take the max of the range and ans
            if s[r] not in seen:
                ans = max(ans, r-l+1)
                
            # if not seen then 2 case:
            # either element included in window, then increase the window size
            # or not included in window, then move left pointer to seen[r] + 1
            
            else:
                if seen[s[r]] < l:
                    ans = max(ans, r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return ans