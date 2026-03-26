
def bridge_and_torch(times):
    times.sort()
    n = len(times)

    dp = [float('inf')] * (n + 1)
    dp[1] = times[0]
    if n > 1:
        dp[2] = times[1]
    if n > 2:
        dp[3] = times[0] + times[1] + times[2]

    for i in range(4, n + 1):
        option1 = times[1] + times[0] + times[i - 1] + times[1]
        option2 = times[i - 1] + times[0] + times[i - 2] + times[0]
        dp[i] = min(dp[i - 2] + option1, dp[i - 2] + option2)

    return dp[n]

if __name__ == "__main__":

    times = [10, 20, 30]
    print(bridge_and_torch(times))