from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # build intervals
        first = {}
        last = {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i

        intervals = [[first[c], last[c]] for c in first]

        # 2. merge intervals
        intervals.sort()
        res = []
        start, end = intervals[0]

        for st, en in intervals:
            if st <= end:
                end = max(end, en)
            else:
                res.append(end - start + 1)
                start, end = st, en

        res.append(end - start + 1)
        return res


s = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(s))