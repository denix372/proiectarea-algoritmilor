
def interval_scheduling(intervals):
    intervals.sort(key = lambda x : x[1])

    count = 0
    end = 0
    res = []

    for i in intervals:
        if (end <= i[0]):
            end = i[1]
            count += 1
            res.append(i)
    return res

intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)] 
print(interval_scheduling(intervals))