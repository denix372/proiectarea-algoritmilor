from collections import defaultdict

class Solution:
    def count_triplets(self, arr: list[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
            
        cnt = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    cnt += (k - i)
                    
        return cnt

class Solution2:
    def count_triplets(self, arr: list[int]) -> int:
        d = defaultdict(int)
        index = defaultdict(int)
        d[0] = 1
        index[0] = 0


        prefix = 0
        cnt = 0

        for i, x in enumerate(arr):
            prefix ^= x

            if prefix in d:
                cnt += d[prefix] * i - index[prefix]
            
            d[prefix] += 1
            index[prefix] += (i + 1)

        return cnt

arr = [2,3,1,6,7]
print(Solution().countTriplets(arr))
print(Solution2().countTriplets(arr))