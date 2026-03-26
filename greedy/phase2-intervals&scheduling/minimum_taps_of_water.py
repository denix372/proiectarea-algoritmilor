class Solution:
    def minTaps(self, n: int, ranges):
        intervals = []

        for i, r in enumerate(ranges):
            intervals.append([max(0, i - r), min(n, i + r)])

        intervals.sort()

        taps = 0
        curr_end = 0
        next_end = 0
        i = 0
        m = len(intervals)

        while curr_end < n:
            while i < m and intervals[i][0] <= curr_end:
                next_end = max(next_end, intervals[i][1])
                i += 1

            if next_end == curr_end:
                return -1

            taps += 1
            curr_end = next_end

        return taps

n = 5
ranges = [3,4,1,1,0,0]

print(Solution().minTaps(n, ranges))