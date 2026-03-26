import sys
MOD = 10**9 + 7
input = sys.stdin.readline

# O(n ^ 2) classic approach
def solve():
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = (dp[i] + dp[j]) % MOD
    print(sum(dp) % MOD)

# O(nlogn) approach with Fenwick Tree
def solve2():
    # 1. Coordinate Compression
    # The numbers can be up to 10^9, but a Fenwick tree needs small indices.
    # We map the unique numbers to ranks: 1, 2, 3...
    sorted_unique = sorted(list(set(nums)))
    rank = {val: i + 1 for i, val in enumerate(sorted_unique)}
    
    # 2. Fenwick Tree (1-indexed)
    # Stores the sum of ways to form sequences ending with a specific rank
    max_rank = len(sorted_unique)
    bit = [0] * (max_rank + 1)
    
    def add(i, val):
        while i <= max_rank:
            bit[i] = (bit[i] + val) % MOD
            i += i & (-i)

    def query(i):
        s = 0
        while i > 0:
            s = (s + bit[i]) % MOD
            i -= i & (-i)
        return s

    total_subsequences = 0
    
    for x in nums:
        r = rank[x]
        
        # How many increasing subsequences can we append 'x' to?
        # Answer: The sum of sequences ending with a rank STRICTLY LESS than 'r'
        # We add 1 for the sequence consisting of just [x] itself.
        ways = (query(r - 1) + 1) % MOD
        total_subsequences = (total_subsequences + ways) % MOD

        # Update the tree: there are now 'ways' more sequences ending at rank 'r'
        add(r, ways)
        
    print(total_subsequences)

n = int(input())
nums = list(map(int, input().split()))
solve2()