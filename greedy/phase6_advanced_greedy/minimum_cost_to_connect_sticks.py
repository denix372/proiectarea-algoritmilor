import heapq

def connect_ropes(ropes: list[int]) -> int:
    if len(ropes) <= 1:
        return 0

    heapq.heapify(ropes)
    total = 0

    while len(ropes) > 1:
        a = heapq.heappop(ropes)
        b = heapq.heappop(ropes)
        cost = a + b
        total += cost
        heapq.heappush(ropes, cost)

    return total

ropes =  [2, 4, 3]
print(connect_ropes(ropes))