def z_traversal(mat):
    if len(mat) == 1:
        print(mat[0][0], end = " ")
        return

    n = len(mat)
    z_traversal([row[: n//2] for row in mat[:n//2]])
    z_traversal([row[n//2:] for row in mat[:n//2]])
    z_traversal([row[:n//2] for row in mat[n//2:]])
    z_traversal([row[n//2:] for row in mat[n//2:]])

mat = [[1, 2, 5, 6],
        [3, 4, 7, 8],
        [9, 10, 13, 14],
        [11, 12, 15, 16]]

z_traversal(mat)