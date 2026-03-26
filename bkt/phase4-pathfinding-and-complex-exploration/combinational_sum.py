


def target_sum_combinations(arr, target):
    n = len(arr)
    res = []

    def back(i, sol, total):
        if total == target:
            res.append(sol.copy())
            return

        if total > target or i > n:
            return
        
        for j in range(i, n):
            if arr[j] + total <= target:
                sol.append(arr[j])
                back(j, sol, total + arr[j])
                sol.pop()
        return
    back(0, [], 0)
    return res

arr = [1, 2, 3]
target = 5
for i in target_sum_combinations(arr, target):
    print(i)