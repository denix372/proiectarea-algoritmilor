class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ls = 0
        rs = 0
        res = 0
        for x in s:
            if x == 'L':
                ls+=1
            else:
                rs += 1
            if ls == rs:
                res += 1
        return res
    
s = "RLRRLLRLRL"
print(Solution().balancedStringSplit(s))