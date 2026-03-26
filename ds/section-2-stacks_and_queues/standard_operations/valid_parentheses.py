class Solution:
    def isValid(self, s: str) -> bool:
        opens = []

        for x in s:
            if x == '(' or x == '[' or x == '{':
                opens.append(x)
            else:
                if not opens:
                    return False
    
                y = opens.pop()
                if y == '(' and x == ')':
                    continue
                elif y == '[' and x == ']':
                    continue
                elif y == '{' and x == '}':
                    continue
                
                return False

        if opens:
            return False
        return True

s = '([)]'
print(Solution().isValid(s))