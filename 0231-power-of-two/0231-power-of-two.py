class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        # iterative approach tc = O(log(n))
        
        # edge case for 0
        if n == 0:
            return False
        
        # we repeat the process till the value is 1
        # if it is other than 1 then not possible
        while n % 2 == 0:
            # all the power of 2 will be divisible by 2
            n /= 2
        return n == 1
        """
        
        """
        # resursive approach
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(n/2)
        return False
        """
        
        # bit manuplation approach
        # ex 8 => 1000
        #    7 => 0111
        #   &---------
        #    0 => 0000
        
        # 10 => 1010
        # 9 =>  1001
        #   &-------
        # 11 => 1011
        
        if n == 0:
            return False
        if n & (n-1) == 0:
            return True
        else:
            return False
        