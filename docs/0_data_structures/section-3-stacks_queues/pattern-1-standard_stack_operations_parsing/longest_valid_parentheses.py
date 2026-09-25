
class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                # If stack is empty, push the current index as a new base marker
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len

print(Solution().longestValidParentheses("(()"))