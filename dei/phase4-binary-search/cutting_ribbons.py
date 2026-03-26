

def cutting_ribbons(ribbons, k):
    if sum(ribbons) < k:
        return 0
    left = 1
    right = max(ribbons)

    def feasible(mid):
        res = 0
        for r in ribbons:
            if res >= k:
                return True
            res += r // mid
        return res >= k

    while left <= right:
        mid = (left + right) // 2

        if feasible(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right


ribbons = [7, 5, 9]
k = 4
print(cutting_ribbons(ribbons, k))