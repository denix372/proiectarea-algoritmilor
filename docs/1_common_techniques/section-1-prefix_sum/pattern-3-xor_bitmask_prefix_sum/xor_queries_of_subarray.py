
class Solution:
    def xor_queries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        res = []
        for l, r in queries:
            res.append(prefix[r + 1] ^ prefix[l])
        return res

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(Solution().xorQueries(arr, queries))