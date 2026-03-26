
def solve(n, m, top, bottom, left, right, rules):

    def valid_adj(i, j, ch):
        if i > 0 and rules[i-1][j] == ch:
            return False
        if i < M-1 and rules[i+1][j] == ch:
            return False
        if j > 0 and rules[i][j-1] == ch:
            return False
        if j < N-1 and rules[i][j+1] == ch:
            return False
        return True

    def check_constraints():
        for i in range(M):
            p = sum(rules[i][j] == '+' for j in range(N))
            n = sum(rules[i][j] == '-' for j in range(N))
            if left[i] != -1 and p != left[i]: return False
            if right[i] != -1 and n != right[i]: return False

        for j in range(N):
            p = sum(rules[i][j] == '+' for i in range(M))
            n = sum(rules[i][j] == '-' for i in range(M))
            if top[j] != -1 and p != top[j]: return False
            if bottom[j] != -1 and n != bottom[j]: return False

        return True

    def bkt(i, j):
        if i == m:
            return check_constraints()
        if j == n:
            return bkt(i + 1, 0)

        cell = rules[i][j]
        if cell == 'L':
            # try +-
            if valid_adj(i, j, '+') and valid_adj(i, j+1, '-'):
                rules[i][j], rules[i][j+1] = '+', '-'
                if bkt(i, j+2): return True
                rules[i][j], rules[i][j+1] = 'L', 'R'

            # try -+
            if valid_adj(i, j, '-') and valid_adj(i, j+1, '+'):
                rules[i][j], rules[i][j+1] = '-', '+'
                if bkt(i, j+2): return True
                rules[i][j], rules[i][j+1] = 'L', 'R'

            # try xx
            rules[i][j], rules[i][j+1] = 'x', 'x'
            if bkt(i, j+2): return True
            rules[i][j], rules[i][j+1] = 'L', 'R'

            return False

        elif cell == 'T':
            # try +-
            if valid_adj(i, j, '+') and valid_adj(i+1, j, '-'):
                rules[i][j], rules[i+1][j] = '+', '-'
                if bkt(i, j+1): return True
                rules[i][j], rules[i+1][j] = 'T', 'B'

            # try -+
            if valid_adj(i, j, '-') and valid_adj(i+1, j, '+'):
                rules[i][j], rules[i+1][j] = '-', '+'
                if bkt(i, j+1): return True
                rules[i][j], rules[i+1][j] = 'T', 'B'

            # try xx
            rules[i][j], rules[i+1][j] = 'x', 'x'
            if bkt(i, j+1): return True
            rules[i][j], rules[i+1][j] = 'T', 'B'

            return False

        else:
            # R or B or already filled
            return bkt(i, j+1)

    bkt(0, 0)
    return rules

M = 5
N = 6
top = [ 1, -1, -1, 2, 1, -1 ]
bottom = [ 2, -1, -1, 2, -1, 3 ]
left = [ 2, 3, -1, -1, -1 ]
right = [ -1, -1, -1, 1, -1 ]

rules = [["L","R","L","R","T","T" ],
                      [ "L","R","L","R","B","B" ],
                      [ "T","T","T","T","L","R" ],
                      [ "B","B","B","B","T","T" ],
                      [ "L","R","L","R","B","B" ]]

for r in solve(N, M, top, bottom, left, right, rules):
    print(*r)
         