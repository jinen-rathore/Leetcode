#User function Template for python3
class Solution:
    def colName (self, n):
        res = ""
        
        while n > 0:
            curr_len = n % 26
            if curr_len == 0: # coz z = 26 and 26 %26 == 0
                curr_len = 26 
                n -= 1
                
            n = n // 26
            
            res += chr(curr_len + 64) # as 65 is A and 90 is Z
        return res[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends