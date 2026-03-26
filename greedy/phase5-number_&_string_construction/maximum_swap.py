class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)

        last = {d: i for i, d in enumerate(digits)}

        for i in range(n):
            for d in range(9, int(digits[i]), -1):
                d = str(d)
                if d in last and last[d] > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num

num = 2736
print(Solution().maximumSwap(num))