from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        # Sort tickets in reverse lexical order before building the graph
        # so that when we pop(), we get the smallest lexical string first.
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        
        # 2. Post-Order DFS
        def dfs(airport):
            # While there are still outgoing flights from this airport
            while graph[airport]:
                # Greedily pick the lexicographically smallest destination
                next_airport = graph[airport].pop()
                dfs(next_airport)
            
            # 3. No more outgoing flights? We hit a dead end, add to itinerary
            itinerary.append(airport)
            
        dfs("JFK")
        
        # 4. The itinerary was built starting from the dead end, so reverse it
        return itinerary[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(Solution().findItinerary(tickets))