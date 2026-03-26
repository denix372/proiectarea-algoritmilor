s = list(input())
n = len(s)
for i in range(n):
    if s[i] == '_':
        for c in "abcdefghijklmnopqrstuvwxyz":
            if (i > 0 and s[i - 1] == c):
                continue
            if (i < n - 1 and s[i + 1] != '_' and s[i + 1] == c):
                continue
            s[i] = c
            break

print("".join(s))