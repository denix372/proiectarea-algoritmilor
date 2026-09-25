

def is_safe(k, i , arr):
    for j in range(k):
        if arr[j] == i or (abs(arr[j] - i) == abs(j - k)):
            return False
    return True

def place_queens(k, n, arr):
    if k == n:
        return 1
    
    for i in range(1, n + 1):
        if isSafe(k, i, arr):
            arr.append(i)

            if placeQueens(k + 1, n, arr) == 1:
                return 1

            arr.pop()

    return 0

def n_queen(n):
    arr = []
    if placeQueens(0, n, arr) == 1:
        return arr
    return [-1]

n = 4
ans = nQueen(n)
for i in ans:
    print(i, end=" ")
print()