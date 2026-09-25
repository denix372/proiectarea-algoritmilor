
from typing import List

class Solution:
    def decode_string(self, s: str) -> str:
        opens = []
        res = ""
        skips = 0

        for x in s:
            if x != ']':
                opens.append(x)
            
            elif x == ']':
                sub = ""
                
                while opens and opens[-1] != '[':
                    sub = opens.pop() + sub
                
                # 2. Pop the '[' itself
                opens.pop()
                
                # 3. Gather multi-digit number (k) from the stack
                k_list = []
                while opens and opens[-1].isdigit():
                    k_list.append(opens.pop())
                
                # Since we popped them right-to-left, reverse them to get the right number
                # e.g., ['2', '1'] becomes "12" -> int -> 12
                n = int("".join(reversed(k_list)))
        
                opens.append(sub * n)

        return "".join(opens)

s = "3[a]2[bc]"
print(Solution().decodeString(s))