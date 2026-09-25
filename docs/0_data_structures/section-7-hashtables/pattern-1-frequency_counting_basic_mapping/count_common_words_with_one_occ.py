from typing import List
from collections import defaultdict
class Solution:
    def count_words(self, words1: List[str], words2: List[str]) -> int:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for x in words1:
            d1[x] += 1
        for x in words2:
            d2[x] += 1
        
        cnt = 0
        for x in d1.keys():
            if x in d2 and d1[x] == 1 and d2[x] == 1:
                cnt += 1
        return cnt

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(Solution().countWords(words1, words2))