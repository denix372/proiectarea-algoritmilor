


n = int(input())
meetings = []
cnt = 0
s = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        meetings.append(b)
        cnt += a
    s += b
x = int(input())


meetings.sort()
for i in range(max(cnt - x, 0)):
    s -= 2 * meetings[i]
print(s)