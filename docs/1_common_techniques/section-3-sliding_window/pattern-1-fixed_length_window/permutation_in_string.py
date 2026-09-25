from collections import defaultdict

class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        d1 = defaultdict(int)
        for x in s1:
            d1[x] += 1
    
        d2 = defaultdict(int)
        for i in range(k):
            d2[s2[i]] += 1
        
        if d1 == d2:
            return True

        for i in range(k, len(s2)):
            d2[s2[i - k]] -= 1
            d2[s2[i]] += 1
            if d2[s2[i - k]] == 0:
                del d2[s2[i - k]]
            
            if d1 == d2:
                return True
        
        return False
            
s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))