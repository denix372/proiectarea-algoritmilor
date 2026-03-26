
def job_sequencing(deadline, profit):
    n = len(deadline)
    jobs = list(zip(deadline, profit))

    jobs.sort(key=lambda x: x[1], reverse=True)

    max_d = max(deadline)
    slot = [False] * (max_d + 1)
    total_profit = 0
    count_jobs = 0

    for d, p in jobs:
        for t in range(d, 0, -1):
            if not slot[t]:
                slot[t] = True
                total_profit += p
                count_jobs += 1
                break

    return count_jobs, total_profit

deadline = [2, 1, 2, 1, 1]
profit   = [100, 19, 27, 25, 15]

print(job_sequencing(deadline, profit))
