
def solve(a, b, s):
    letters = list(set(a + b + s))
    n = len(letters)

    assign = {}
    used = [False] * 10

    def to_num(word):
        return int("".join(str(assign[c]) for c in word))

    def bkt(i):
        if i == n:
            return to_num(a) + to_num(b) == to_num(s)

        ch = letters[i]

        for d in range(10):
            if used[d]:
                continue

            if d == 0 and (ch == a[0] or ch == b[0] or ch == s[0]):
                continue

            assign[ch] = d
            used[d] = True

            if bkt(i + 1):
                return True

            used[d] = False
            del assign[ch]
        return False
    if bkt(0):
        return to_num(a), to_num(b), to_num(s)
    return -1

a = "SEND"
b = "MORE"
s = "MONEY"
print(solve(a, b, s))