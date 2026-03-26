# python program to count number of ways to arrange three
# types of balls such that no two balls of same color
# are adjacent to each other using tabulation


def countWays(p, q, r):
  
    # Create 3 3D DP tables (p+1) x (q+1) x (r+1) using lists
    dpp = [[[0 for _ in range(r + 1)]
               for _ in range(q + 1)] for _ in range(p + 1)]
    dpq = [[[0 for _ in range(r + 1)]
               for _ in range(q + 1)] for _ in range(p + 1)]
    dpr = [[[0 for _ in range(r + 1)]
               for _ in range(q + 1)] for _ in range(p + 1)]

    # Base cases for when only one ball of each type is left
    # Only p left and the last ball is p
    dpp[1][0][0] = 1

    # Only q left and the last ball is q
    dpq[0][1][0] = 1

    # Only r left and the last ball is r
    dpr[0][0][1] = 1

    # Iteratively fill the DP table
    for i in range(p + 1):
        for j in range(q + 1):
            for k in range(r + 1):
                # If the count of balls is zero, skip
                if i == 0 and j == 0 and k == 0:
                    continue

                # Last ball was P, so next can be Q or R
                if i > 0:
                    dpp[i][j][k] += dpq[i - 1][j][k]
                    dpp[i][j][k] += dpr[i - 1][j][k]

                # Last ball was Q, so next can be P or R
                if j > 0:
                    dpq[i][j][k] += dpp[i][j - 1][k]
                    dpq[i][j][k] += dpr[i][j - 1][k]

                    # Last ball was R, so next can be P or Q
                if k > 0:
                    dpr[i][j][k] += dpp[i][j][k - 1]
                    dpr[i][j][k] += dpq[i][j][k - 1]

    # The answer is the sum of all configurations
    # for the given p, q, r
    ans = dpp[p][q][r] + dpq[p][q][r] + dpr[p][q][r]
    return ans

if __name__ == "__main__":
    p, q, r = 1, 1, 1
    print(countWays(p, q, r))