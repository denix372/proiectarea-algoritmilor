from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heappush(self.small, - num)

        if self.small and self.large and (- self.small[0]) > self.large[0]:
            val = - heappop(self.small)
            heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = - heappop(self.small)
            heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = - heappop(self.large)
            heappush(self.small, val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return - self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        
        return (- self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0