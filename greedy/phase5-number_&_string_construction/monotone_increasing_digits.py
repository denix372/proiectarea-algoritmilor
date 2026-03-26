

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))
        length = len(digits)

        changed = True
        while changed:
            changed = False

            for i in range(1, length):
                if digits[i] < digits[i - 1]:
                    digits[i - 1] -= 1

                    for j in range(i, length):
                        digits[j] = 9

                    changed = True
                    break

        return int("".join(map(str, digits)))

n = 332
print(Solution().monotoneIncreasingDigits(n))