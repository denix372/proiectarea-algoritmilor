def equalPartition(arr):
    n = len(arr)
    total = sum(arr)

    target = 0
    sol = []
    res = [[], []]

    def back(i, sol):
        nonlocal target
        n = len(arr)

        if (target == total // 2 and 
            ((n % 2 == 0 and len(sol) == n // 2) or
            (n % 2 != 0 and (len(sol) == n // 2 or
            len(sol) == n // 2 + 1)))):
            return True
        
        if i >= n:
            return False
        
        sol.append(i)
        target += arr[i]

        if back(i + 1, sol):
            return True

        target -= arr[i]
        sol.pop()

        if back(i + 1, sol):
            return True
        
        return False
    
    if back(0, sol):
        k = 0
        for i in range(n):
            if k < len(sol) and i == sol[k]:
                res[0].append(arr[i])
                k += 1
            else:
                res[1].append(arr[i])
    return res

arr = [1, 2, 3,4]
res = equalPartition(arr)

for subset in res:
    print(" ".join(map(str, subset)))