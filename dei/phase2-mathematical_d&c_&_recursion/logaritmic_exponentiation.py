

def log_exp(base, exp, MOD):
    res = 1
    base = base % MOD

    while exp > 0:
        if exp & 1 :                    # if exp % 2 == 1
            res = (res * base) % MOD
        base = (base * base) % MOD
        exp = exp >> 1                  # exp = exp//2
    return res

print(log_exp(2.0, 3434343, 255))