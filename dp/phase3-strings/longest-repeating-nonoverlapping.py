def solve(s):
    n = len(s)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    res = 0
    end_index = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            
            # if characters match AND the overlap condition holds
            if s[i - 1] == s[j - 1] and dp[i - 1][j - 1] < (j - i):
                dp[i][j] = dp[i - 1][j - 1] + 1
                
                if dp[i][j] > res:
                    res = dp[i][j]
                    # We save 'i' because it represents the end of the 
                    # FIRST occurrence of the repeating string
                    end_index = i 
            else:
                dp[i][j] = 0
                
    if res > 0:
        return s[end_index - res : end_index]
    return "-1"

# O(nlogn) solution with BinSearch and Rabin-Karp (Rolling Hash)
def solve2(s):
    n = len(s)
    
    # Helper function to check if a valid substring of a specific 'length' exists
    def check(length: int) -> int:
        if length == 0: return -1
        
        base = 31
        mod = 10**9 + 7
        
        # Highest power of base for the rolling hash
        base_L = pow(base, length, mod)
        
        # Compute hash for the first window of size 'length'
        current_hash = 0
        for i in range(length):
            current_hash = (current_hash * base + ord(s[i])) % mod
            
        # Dictionary to store {hash_value : starting_index}
        # We only store the FIRST time we see a hash to maximize distance
        seen = {current_hash: 0}
        
        for i in range(1, n - length + 1):
            # Rolling Hash Math: Remove outgoing char, add incoming char
            current_hash = (current_hash * base - ord(s[i - 1]) * base_L + ord(s[i + length - 1])) % mod
            
            if current_hash in seen:
                # Overlap check: is the current index far enough from the first occurrence?
                if i - seen[current_hash] >= length:
                    # Double-check exact string to prevent extremely rare hash collisions
                    if s[seen[current_hash] : seen[current_hash] + length] == s[i : i + length]:
                        return seen[current_hash]
            else:
                # Only record the first time we see this hash!
                seen[current_hash] = i
                
        return -1

    # Binary Search on the length of the substring
    left = 1
    right = n // 2
    best_start = -1
    max_len = 0

    while left <= right:
        mid = (left + right) // 2
        
        start_index = check(mid)
        if start_index != -1:
            # We found a match! Try to find a longer one.
            best_start = start_index
            max_len = mid
            left = mid + 1
        else:
            # No match found. We must look for shorter lengths.
            right = mid - 1
            
    if max_len > 0:
        return s[best_start : best_start + max_len]
    return "-1"

s = "acdcdacdc"
print(solve(s))
print(solve2(s))