class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n == 2:
            return x * x
        
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n > 0:
            if n & 1:
                res *= x
            x = x * x
            n >>= 1
        return res

x = 2.00000
n = -2
print(Solution().myPow(x, n))