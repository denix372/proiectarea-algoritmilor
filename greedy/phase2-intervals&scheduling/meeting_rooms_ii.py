

def solve(intervals):
    intervals.sort(key = lambda x : x[1])
    count = 0
    end = 0
    for i in intervals:
        if end < i[0]:
            count += 1
            end = i[1]
    return len(intervals) - count + 1


# for [a, b], [c, d], with a < c 2 intervals
# intervals overlapp fi 1. c <= b 
#                       2. b <= d

intervals = [[0, 30],[5, 10],[15, 20]]
print(solve(intervals))