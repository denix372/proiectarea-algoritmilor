MOD = 10**9 + 7

def solve(nums):
    dp_even = 1 # multimea vida
    dp_odd = 0

    for x in nums:
        if x % 2 == 0:
            dp_even, dp_odd = (dp_even * 2) % MOD, (dp_odd * 2) % MOD
        else:
            new_even = (dp_even + dp_odd) % MOD
            new_odd  = (dp_even + dp_odd) % MOD
            dp_even, dp_odd = new_even, new_odd

    return (dp_even - 1) % MOD

def solve1(nums):
    n = len(nums)
    dp_even = [0] * (n + 1)
    dp_odd  = [0] * (n + 1)
    dp_even[0] = 1   # doar multimea vida
    for i in range(1, n + 1):
        if nums[i - 1] % 2 == 0:
            dp_even[i] = (dp_even[i-1] * 2) % MOD
            dp_odd[i]  = (dp_odd[i-1]  * 2) % MOD
        else:
            s = (dp_even[i-1] + dp_odd[i-1]) % MOD
            dp_even[i] = s
            dp_odd[i]  = s

    return (dp_even[n] - 1) % MOD


def solve2(nums):
    odd = sum(x & 1 for x in nums)
    if odd == 0:
        return ((pow(2, n, MOD) - 1) % MOD)
    else:
        return ((pow(2, n - 1, MOD) - 1) % MOD)

with open("azerah.in") as fin:
    t = int(fin.readline())
    out = []

    for _ in range(t):
        n = int(fin.readline())
        nums = list(map(int, fin.readline().split()))
        out.append(solve1(nums))

with open("azerah.out", "w") as fout:
    for ans in out:
        fout.write(str(ans) + "\n")
