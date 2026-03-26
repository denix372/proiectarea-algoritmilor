
import sys
sys.setrecursionlimit(200000)

def get_all_heights(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    in1 = [0] * n  # The maximum depth in the subtree
    in2 = [0] * n  # The second maximum depth in the subtree
    c1 = [-1] * n  # The child node that gave the max depth (in1)
    out = [0] * n  # The maximum depth outside the subtree (going up)

    def dfs_in(u, p):
        for v in adj[u]:
            if v == p:
                continue
            
            dfs_in(v, u)
            
            # The height from 'u' going down to 'v'
            h = in1[v] + 1
            
            # Update the top 2 heights for node 'u'
            if h > in1[u]:
                in2[u] = in1[u]
                in1[u] = h
                c1[u] = v
            elif h > in2[u]:
                in2[u] = h

    def dfs_out(u, p):
        for v in adj[u]:
            if v == p:
                continue
                
            # If 'v' is the branch that gave 'u' its maximum in-height,
            # 'u' cannot use in1 to go down to 'v' (that's a U-turn).
            # It must use its second-best branch (in2) or go further up (out).
            if c1[u] == v:
                longest_path_away_from_v = max(out[u], in2[u])
            else:
                longest_path_away_from_v = max(out[u], in1[u])
    
            # The out-height of 'v' is 1 step to 'u' + the longest path away from 'v'
            out[v] = 1 + longest_path_away_from_v
            
            dfs_out(v, u)

    # Execute the two passes starting from an arbitrary root (node 0)
    dfs_in(0, -1)
    dfs_out(0, -1)

    res = [max(in1[i], out[i]) for i in range(n)]
    return max(res)

def solve(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def dfs(u, p, d, dist_array):
        dist_array[u] = d
        for v in adj[u]:
            if v != p: 
                dfs(v, u, d + 1, dist_array)

    dist_from_0 = [0] * n
    dfs(0, -1, 0, dist_from_0)
    
    node_A = max(range(n), key=lambda i: dist_from_0[i])
    
    dist_from_A = [0] * n
    dfs(node_A, -1, 0, dist_from_A)
    node_B = max(range(n), key=lambda i: dist_from_A[i])
    
    dist_from_B = [0] * n
    dfs(node_B, -1, 0, dist_from_B)
    
    res = [max(dist_from_A[i], dist_from_B[i]) for i in range(n)]
    
    return max(res)

n = 11
edges = [ (0, 1), (0, 2), (0, 3),   
        (1, 4), (1, 5),           
        (2, 6),                  
        (3, 7), (3, 8),          
        (6, 9), (6, 10)]

heights = get_all_heights(n, edges)
print(get_all_heights(n, edges))
print(solve(n, edges))