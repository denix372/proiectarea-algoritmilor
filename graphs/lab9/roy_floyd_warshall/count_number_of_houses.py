from typing import List
INF = 10**9
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                d = min(j - i, abs(i - x) + 1 + abs(j - y),
                                abs(i - y) + 1 + abs(j - x))
                res[d] += 2
        return res[1:]

n =3
x =1
y =3
print(Solution().countOfPairs(n, x, y))