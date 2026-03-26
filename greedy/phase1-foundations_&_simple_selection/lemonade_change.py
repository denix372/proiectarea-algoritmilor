from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
    
        for x in bills:
            if x == 5:
                fives += 1
            elif x == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            elif x == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
        
bills = [5,5,5,10,20]
print(Solution().lemonadeChange(bills))