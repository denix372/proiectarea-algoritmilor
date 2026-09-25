from typing import List

class Solution:
    def reconstruct_queue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        if n == 0:
            return []

        people.sort(key=lambda x: (x[0], -x[1]))
        res = [None] * n
        tree = [0] * (4 * n)
        
        def build(node, start, end):
            if start == end:
                tree[node] = 1
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = tree[2 * node] + tree[2 * node + 1]
            
        def query_and_update(node, start, end, empty_spots_needed):
            tree[node] -= 1 
            
            if start == end:
                return start
                
            mid = (start + end) // 2
            left_empty = tree[2 * node]
            
            if left_empty >= empty_spots_needed:
                return query_and_update(2 * node, start, mid, empty_spots_needed)
            else:
                return query_and_update(2 * node + 1, mid + 1, end,
                        empty_spots_needed - left_empty)

        build(1, 0, n - 1)
        
        for h, k in people:
            idx = query_and_update(1, 0, n - 1, k + 1)
            res[idx] = [h, k]
            
        return res

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))