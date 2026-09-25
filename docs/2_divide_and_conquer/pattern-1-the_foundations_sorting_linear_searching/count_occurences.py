from bisect import bisect_left, bisect_right

class Solution:
    def count_freq(self, arr, target):
        # code here
        i = bisect_left(arr, target)
        j = bisect_right(arr, target)
        return j - i