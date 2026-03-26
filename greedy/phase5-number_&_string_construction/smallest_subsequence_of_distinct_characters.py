class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c not in in_stack:
                while stack and stack[-1] > c and last[stack[-1]] > i:
                    removed = stack.pop()
                    in_stack.remove(removed)

                stack.append(c)
                in_stack.add(c)

        return ''.join(stack)


s = "bcabc"
print(Solution().smallestSubsequence(s))