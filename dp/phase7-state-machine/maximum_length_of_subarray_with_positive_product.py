from typing import List
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        poz = [0] * n
        neg = [0] * n
        
        # Base case for the first element
        if nums[0] > 0:
            poz[0] = 1
        elif nums[0] < 0:
            neg[0] = 1

        for i in range(1, n):
            if nums[i] > 0:
                # Positive number extends a positive length naturally
                poz[i] = poz[i - 1] + 1

                # It can only extend a negative length if one already exists
                if neg[i - 1] > 0:
                    neg[i] = neg[i - 1] + 1
                else:
                    neg[i] = 0
                    
            elif nums[i] < 0:
                # Negative number flips the negative length to positive
                # ONLY if a negative length already exists!
                if neg[i - 1] > 0:
                    poz[i] = neg[i - 1] + 1
                else:
                    poz[i] = 0
                    
                # Negative number flips the positive length to negative
                # Even if poz[i-1] is 0, 0 + 1 = 1, which is correct (a single negative number)
                neg[i] = poz[i - 1] + 1
                
            else:
                # If we hit a 0, the product becomes 0. 
                # We must reset our lengths and start fresh.
                poz[i] = 0
                neg[i] = 0
                
        return max(poz)

nums = [1,-2,-3,4]
print(Solution().getMaxLen(nums))