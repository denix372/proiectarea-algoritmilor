
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Merge previous smaller or equal prices into the current span
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
            
        # Push the current price and its accumulated span onto the stack
        self.stack.append((price, span))
        
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

stockSpanner = StockSpanner();
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60))
print(stockSpanner.next(75))
print(stockSpanner.next(85))