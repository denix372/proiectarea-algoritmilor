import sys

# DP Approach
def minimal_grid_path(n, matrix):
    dp = [[""] * n for i in range(n)]
    dp[0][0] = matrix[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]
        dp[0][i] = dp[0][i - 1] + matrix[0][i]

    for i in range(1, n):
        for j in range(1, n):
            # Comparing strings is O(N), making this O(N^3) total
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j] 
            
    return dp[n - 1][n - 1]

 
def minimal_grid_path2(n, matrix):
    # res stores the characters of the best path found so far
    res = [matrix[0][0]]
    
    # current_cells stores the row indices 'r' of the best positions 
    # on the current diagonal. (On a diagonal, r + c = constant)
    current_cells = [0]
    
    # A path in an n x n grid has 2n - 1 characters. 
    # We already have the first one, so we need 2n - 2 more steps.
    for d in range(2 * n - 2):
        min_char = '{'  # Initialize with a character lexicographically larger than 'Z'
        
        # Step 1: Identify the smallest character available in the next diagonal
        for r in current_cells:
            c = d - r
            # Option 1: Move Right (r, c + 1)
            if c + 1 < n:
                if matrix[r][c + 1] < min_char:
                    min_char = matrix[r][c + 1]
            # Option 2: Move Down (r + 1, c)
            if r + 1 < n:
                if matrix[r + 1][c] < min_char:
                    min_char = matrix[r + 1][c]
        
        res.append(min_char)
        
        # Step 2: Collect all row indices for the next diagonal that match min_char
        next_cells = []
        for r in current_cells:
            c = d - r
            
            # Check Right
            if c + 1 < n and matrix[r][c + 1] == min_char:
                # Avoid adding the same cell twice
                if not next_cells or next_cells[-1] != r:
                    next_cells.append(r)
            
            # Check Down
            if r + 1 < n and matrix[r + 1][c] == min_char:
                # Avoid adding the same cell twice
                if not next_cells or next_cells[-1] != r + 1:
                    next_cells.append(r + 1)
                    
        current_cells = next_cells
        
    return "".join(res)


def main():
    # Read n first
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())
    
    # Read exactly n lines for the matrix
    # This lets the program finish as soon as you hit Enter on the last line
    matrix = []
    for _ in range(n):
        matrix.append(sys.stdin.readline().strip())
    
    # Call your function and print
    print(minimal_grid_path2(n, matrix))

if __name__ == "__main__":
    main()