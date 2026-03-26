from collections import defaultdict
class Solution:
    def secFrequent(self, arr):
        # code here
        d = defaultdict(int)
        for x in arr:
            d[x] += 1
    
        max1 = -1
        max2 = -1

        unique_freqs = set(d.values())

        for freq in unique_freqs:
            if freq > max1:
                max2 = max1
                max1 = freq
            elif freq > max2 and freq < max1:
                max2 = freq

        return max2 if max2 != -1 else -1
arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
print(Solution().secFrequent(arr))