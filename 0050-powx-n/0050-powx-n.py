class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case of recursion
        if n == 0:
            return 1
        
        # to handle negative numbers
        if n < 0:
            # we invert the x(the number) and raise it to -n to make n positive 
            return self.myPow(1/x, -n)
        else:
            # checking if n is even
            if n % 2 == 0:
                # the we half the power by squring the x and raising it to half power
                # this makes if faster
                return self.myPow(x*x, n//2)
            # if n is odd
            else:
                # we just do the same
                return self.myPow(x*x, (n-1)//2) * x