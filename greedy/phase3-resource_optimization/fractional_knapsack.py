class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        n = len(val)
        items = [[val[i], wt[i]] for i in range(n)]
        items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
        res = 0.0
        currentCapacity = capacity
    
        for i in range(n):
    
            if items[i][1] <= currentCapacity:
                res += items[i][0]
                currentCapacity -= items[i][1]
            else:
                res += (1.0 * items[i][0] / items[i][1]) * currentCapacity
                break
    
        return res

val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

print(Solution().fractionalKnapsack(val, wt, capacity))