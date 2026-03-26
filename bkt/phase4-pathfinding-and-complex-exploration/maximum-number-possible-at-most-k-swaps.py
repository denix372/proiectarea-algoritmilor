# Approach 1
def maximum_number(s, k):
    n = len(s)
    sol = s

    for i in range(n - 1):
        for j in range(i + 1, n):

            if s[i] < s[j]:

                swapped = list(s)
                swapped[i], swapped[j] = swapped[j], swapped[i]
                swapped = ''.join(swapped)

                res = maximum_number(swapped, k - 1)
                if res > sol:
                    sol = res
    return sol

#Approach 2
def match(sol, res):
    if sol > res:
        res = sol
    return res

def swap(s, i , j):
    swapped = list(s)
    swapped[i], swapped[j] = swapped[j], swapped[i]
    return ''.join(swapped)

def set_digit(s, index, res, k):
    if k == 0 or index == len(s) - 1:
        res = match(s, res)

    maxDigit = 0

    for i in range(index, len(s)):
        maxDigit = max(maxDigit, int(s[i]))

    for i in range(index + 1, len(s)):
        if int(s[i]) == maxDigit:
            s = swap(s, index, i)
            res = set_digit(s, index + 1, res, k - 1)
            s = swap(s, index, i)

    return res


s = "7599"
k = 2
print(maximum_number(s, k))
print(set_digit(s, 0, s, k))