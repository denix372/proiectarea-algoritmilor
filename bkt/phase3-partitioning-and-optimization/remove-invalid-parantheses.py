from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()

        # 1. calculate how many parantheses must be remove
        left_rem = right_rem = 0
        for c in s:
            if c == '(':
                left_rem += 1
            elif c == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        def bkt(index, left_count, right_count, left_rem, right_rem, path):
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and left_count == right_count:
                    res.add("".join(path))
                return

            c = s[index]

            # 2. try to remove the current character
            if c == '(' and left_rem > 0:
                bkt(index + 1, left_count, right_count, left_rem - 1, right_rem, path)

            if c == ')' and right_rem > 0:
                bkt(index + 1, left_count, right_count, left_rem, right_rem - 1, path)

            # 3. keep the current character
            path.append(c)

            if c not in "()":
                bkt(index + 1, left_count, right_count, left_rem, right_rem, path)

            elif c == '(':
                bkt(index + 1, left_count + 1, right_count, left_rem, right_rem, path)

            elif c == ')' and right_count < left_count:
                bkt(index + 1, left_count, right_count + 1, left_rem, right_rem, path)

            # 4. backtrack
            path.pop()

        bkt(0, 0, 0, left_rem, right_rem, [])
        return list(res)

s = "()())()"
sol = Solution()
print(sol.removeInvalidParentheses(s))