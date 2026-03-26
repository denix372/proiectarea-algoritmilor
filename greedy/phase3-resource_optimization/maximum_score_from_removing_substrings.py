class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            first = ("ab", x)
            second = ("ba", y)
        else:
            first = ("ba", y)
            second = ("ab", x)

        def remove_substring(s, sub, val):
            stack = []
            score = 0
            a, b = sub[0], sub[1]

            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += val
                else:
                    stack.append(ch)

            return "".join(stack), score

        s, score1 = remove_substring(s, first[0], first[1])
        _, score2 = remove_substring(s, second[0], second[1])

        return score1 + score2

s = "cdbcbbaaabab"
x = 4
y = 5
print(Solution().maximumGain(s, x, y))