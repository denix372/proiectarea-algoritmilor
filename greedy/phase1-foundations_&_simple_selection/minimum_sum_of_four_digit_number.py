class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list(map(int, str(num)))
        digits.sort()
        num1 = digits[0] * 10 + digits[2]
        num2 = digits[1] * 10 + digits[3]
        return num1 + num2
        
print(Solution().minimumSum(2932))