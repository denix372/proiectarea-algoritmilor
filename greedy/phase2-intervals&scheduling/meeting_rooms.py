

def solve(intervals):
    intervals.sort(key = lambda x : x[1])
    end = 0
    count = 0

    for i in intervals:
        if end < i[0]:
            end = i[1]
            count += 1
    return count == len(intervals)


intervals =  [[0,30],[5,10],[15,20]]
print(solve(intervals))
