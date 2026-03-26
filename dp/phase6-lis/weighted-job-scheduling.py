# Utility function for binary search
def findNextJob(jobs, i):
    low, high = i + 1, len(jobs) - 1
    ans = len(jobs)
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][0] >= jobs[i][1]:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# Function to find maximum profit using tabulation
def maxProfit(jobs):
    jobs.sort()
    n = len(jobs)
    dp = [0] * (n + 1)

    # Build dp table from end
    for i in range(n - 1, -1, -1):
        j = findNextJob(jobs, i)
        dp[i] = max(jobs[i][2] + dp[j],  dp[i + 1])

    return dp[0]

jobs = [
    [1, 2, 50],
    [3, 5, 20],
    [6, 19, 100],
    [2, 100, 200]
]
print(maxProfit(jobs))
