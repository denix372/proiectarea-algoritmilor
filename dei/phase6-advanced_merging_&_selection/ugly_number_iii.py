import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // math.gcd(a, b)
        ac = a * c // math.gcd(a, c)
        bc = b * c // math.gcd(b, c)
        abc = ab * c // math.gcd(ab, c)

        def count(x):
            return (x // a) + (x // b) + (x // c) \
                 - (x // ab) - (x // ac) - (x // bc) \
                 + (x // abc)

        lo, hi = 1, 2 * 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) < n:
                lo = mid + 1
            else:
                hi = mid

        return lo
        
n = 3
a = 2
b = 3
c = 5
print(Solution().nthUglyNumber(n, a, b, c))