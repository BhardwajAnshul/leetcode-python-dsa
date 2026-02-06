class Solution:
    def myPow(self, x: float, n: int) -> float:

        def pow(x, n):
            if x ==0:
                return 0
            if n==0:
                return 1
            res = pow(x, n//2)

            if n%2==0:
                return res*res
            else:
                return res*res*x

        r = pow(x, abs(n))
    

        if n < 0:
            return 1/r
        else:
            return r

        